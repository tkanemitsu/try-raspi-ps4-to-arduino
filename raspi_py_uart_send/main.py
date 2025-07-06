import time

import serial


def main():
    ser = serial.Serial(
        "/dev/serial0",
        750,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1,
    )
    ser.write(b"a")
    time.sleep(0.2)
    ser.write(b"b")
    time.sleep(0.2)
    ser.write(b"c")
    # line = ser.readline()
    # print(line.decode())


if __name__ == "__main__":
    main()
