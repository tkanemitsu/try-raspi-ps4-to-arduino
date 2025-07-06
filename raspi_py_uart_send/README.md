# RasPi から Arduino を UART で制御するサンプル (Python)

RasPi から Python (pyserialライブラリ) を用いて Arduino に UART でデータ送信するサンプルです。

事前に Arduino 側で UART を待ち受けるソフトウェアを起動しておきます。

## RasPi の UART を有効化する

```sh
sudo raspi-config
```

`3 Interface Options` > `I6 Serial Port` > No > Yes と選択。

/boot/firmware/config.txt に設定行 `enable_uart=1` が追記されます。

設定を変更したら reboot コマンドで再起動します。


## 実行手順

1. 後述の通り配線を行う。
2. arduino_uart_recv/ を Arduino IDE で Arduino に書き込み、実行。Serial Monitor を開き baudrate をソースコード記載の値 (例: 9600) に設定。
3. raspi_py_ps4_recv/ を ssh などで RasPi に送り込む。uv sync して uv run main.py でスクリプトを実行。
4. Arduino IDE 上の Serial Monitor で受信したデータを確認。


## RasPi ピン配置

https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio

UART: 3.3V

## Arduino ピン配置

https://docs.arduino.cc/retired/boards/arduino-uno-rev3-with-long-pins/#pinout-diagram

UART: 5V


## 配線

![](./circuit.drawio.svg)


## 課題

* baudrate 750 では送信できたが、9600 や 1200 では送信に失敗。高速化と安定性改善のため、要因調査が必要。
* プルアップ抵抗は 4.7K でよいか。そもそも必要か。
* UARTとして使えるピンの把握。
* C/C++化。


### 補足: baudrate 9600 や 1200 のときの受信内容 (要調査)

| RasPi TX | Arduino RX            |
| :------- | :-------------------- |
| 'a' (97) | 0x02 (2), 0xFE (254)  |
| 'b' (98) | 0x0C (12), 0xFE (254) |
| 'c' (99) | 0x0E (14), 0xFE (254) |

* RasPi から 1 byte を送信したとき、Arduino で 2 byte が受信される。受信は例えば 'a' に対して 0x02, 0xFE の順で得られる。
* 稀に正しく Arduino で 1 byte が受信されることがある。
