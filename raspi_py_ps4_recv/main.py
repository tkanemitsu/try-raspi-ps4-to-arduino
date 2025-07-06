import logging
import sys
import threading
import time

from evdev import InputDevice, InputEvent, ecodes, list_devices

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Ref:
# - Naming: https://controller.dl.playstation.net/controller/lang/en/2100002.html
PS4_EVENT_DICT: dict[int, dict[int, str]] = {
    # 同期
    ecodes.EV_SYN: {},
    # ボタン (0 or 1)
    ecodes.EV_KEY: {
        304: "KEY_BOTTOM_CROSS",
        305: "KEY_RIGHT_CIRCLE",
        307: "KEY_TOP_TRIANGLE",
        308: "KEY_LEFT_SQUARE",
        310: "KEY_L1",
        311: "KEY_R1",
        312: "KEY_L2",  # also triggers ABS_L2
        313: "KEY_R2",  # also triggers ABS_R2
        314: "KEY_SHARE",
        315: "KEY_OPTIONS",
        316: "KEY_PS",
        317: "KEY_L_STICK",
        318: "KEY_R_STICK",
    },
    # スティック (相対軸)
    ecodes.EV_REL: {},
    # スティック (絶対軸, 0-255)
    ecodes.EV_ABS: {
        0: "ABS_L_STICK_X",  # 0: left, 255: right
        1: "ABS_L_STICK_Y",  # 0: top, 255: bottom
        2: "ABS_L2",
        3: "ABS_R_STICK_X",  # 0: left, 255: right
        4: "ABS_R_STICK_Y",  # 0: top, 255: bottom
        5: "ABS_R2",
        16: "ABS_HAT0X",  # -1: left, 0: neutral, 1: right
        17: "ABS_HAT0Y",  # -1: top, 0: neutral, 1: bottom
    },
}

DUAL_SHOCK_VENDOR_ID = 0x054C  # Sony Corp.
DUAL_SHOCK_PRODUCT_ID = 0x09CC  # DualShock 4 [CUH-ZCT2x]


def _get_event_name(event: InputEvent) -> str | None:
    if event.type == ecodes.EV_SYN:
        return None
    code2name = PS4_EVENT_DICT.get(event.type)
    if code2name is None:
        logging.warning(
            "unknown type: type=%d code=%d value=%d",
            event.type,
            event.code,
            event.value,
        )
        return None

    name = code2name.get(event.code)
    if name is None:
        logging.warning(
            "unknown code: type=%d code=%d value=%d",
            event.type,
            event.code,
            event.value,
        )
        return None

    return name


def main() -> int:
    logging.info("==== Print input devices ====")
    devices: list[InputDevice[str]] = []
    for path in list_devices("/dev/input"):
        dev = InputDevice(path)
        logging.info("%s %s", dev.path, dev.name)
        logging.info("- capabilities: %s", dev.capabilities())
        logging.info("- info %s", dev.info)
        logging.info("- phys %s", dev.phys)
        logging.info("- uniq %s", dev.uniq)
        logging.info("- version %s", dev.version)
        devices.append(dev)

    logging.info("==== Select input devices ====")
    gamepad = None
    for dev in devices:
        if (
            dev.info.vendor == DUAL_SHOCK_VENDOR_ID
            and dev.info.product == DUAL_SHOCK_PRODUCT_ID
            and dev.name == "Wireless Controller"
            and gamepad is None  # select first device.
        ):
            gamepad = dev
            logging.info("select %s", dev.path)
            # Note:
            # A connected PS4 wireless controller can be seen as multiple devices such as:
            # - /dev/input/event2 (name = "Wireless Controller")
            # - /dev/input/event3 (name = "Wireless Controller Motion Sensors")
            # - /dev/input/event4 (name = "Wireless Controller Touchpad")
            #
            # Selecting first device intended to select the "Wireless Controller", capturing button operations.
        else:
            dev.close()
    del devices
    if gamepad is None:
        logging.error("No PS4 wireless controller found.")
        return 1

    # shared state
    lock = threading.Lock()
    state: dict[str, int] = {}

    def read_loop():
        # イベントを受け取る
        for event in gamepad.read_loop():
            assert isinstance(event, InputEvent)
            name = _get_event_name(event)
            if name is not None:
                with lock:
                    state[name] = event.value

    logging.info("==== Start read_loop thread ====")
    th = threading.Thread(target=read_loop, daemon=True)
    th.start()

    logging.info("==== Start main loop ====")
    while True:
        time.sleep(0.1)
        with lock:
            print(state)

    # th.join()


if __name__ == "__main__":
    sys.exit(main())
