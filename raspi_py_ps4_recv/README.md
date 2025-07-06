# PS4ワイヤレスコントローラーの入力を受け取るサンプル (Python)

スクリプト main.py は PS4 ワイヤレスコントローラーの操作を evdev ライブラリで取得し、0.1 秒間隔でコントローラー入力状態を出力します。


## 前提

* RaspiとPS4ワイヤレスコントローラーはスクリプト実行前にペアリングしておいてください。ペアリングの方法はトップの README.md に記載しています。


## Python実行環境の初期化

Python の環境構築に [uv](https://docs.astral.sh/uv/getting-started/installation/) を使用します。
公式ドキュメントに従い Raspi に uv をインストールします。

その後、仮想環境をセットアップします。

```sh
cd raspi_py_ps4_recv

# 仮想環境を構築し、Pythonパッケージをインストール
uv sync
```


## スクリプトの実行

```sh
# 仮想環境の中で main.py を実行
uv run main.py
```


## 参考: PS4ワイヤレスコントローラーの接続情報例

```txt
2025-07-06 11:20:09 [INFO] /dev/input/event2 Wireless Controller
2025-07-06 11:20:09 [INFO] - capabilities: {0: [0, 1, 3, 21], 1: [304, 305, 307, 308, 310, 311, 312, 313, 314, 315, 316, 317, 318], 3: [(0, AbsInfo(value=126, min=0, max=255, fuzz=0, flat=0, resolution=0)), (1, AbsInfo(value=128, min=0, max=255, fuzz=0, flat=0, resolution=0)), (2, AbsInfo(value=0, min=0, max=255, fuzz=0, flat=0, resolution=0)), (3, AbsInfo(value=117, min=0, max=255, fuzz=0, flat=0, resolution=0)), (4, AbsInfo(value=128, min=0, max=255, fuzz=0, flat=0, resolution=0)), (5, AbsInfo(value=0, min=0, max=255, fuzz=0, flat=0, resolution=0)), (16, AbsInfo(value=0, min=-1, max=1, fuzz=0, flat=0, resolution=0)), (17, AbsInfo(value=0, min=-1, max=1, fuzz=0, flat=0, resolution=0))], 21: [80, 81, 88, 89, 90, 96]}
2025-07-06 11:20:09 [INFO] - info bus: 0005, vendor 054c, product 09cc, version 8100
2025-07-06 11:20:09 [INFO] - phys 
2025-07-06 11:20:09 [INFO] - uniq XX:XX:XX:XX:XX:XX
2025-07-06 11:20:09 [INFO] - version 65537

2025-07-06 11:20:09 [INFO] /dev/input/event3 Wireless Controller Motion Sensors
2025-07-06 11:20:09 [INFO] - capabilities: {0: [0, 3, 4], 3: [(0, AbsInfo(value=41, min=-32768, max=32768, fuzz=16, flat=0, resolution=8192)), (1, AbsInfo(value=7907, min=-32768, max=32768, fuzz=16, flat=0, resolution=8192)), (2, AbsInfo(value=1873, min=-32768, max=32768, fuzz=16, flat=0, resolution=8192)), (3, AbsInfo(value=-686, min=-2097152, max=2097152, fuzz=16, flat=0, resolution=1024)), (4, AbsInfo(value=1057, min=-2097152, max=2097152, fuzz=16, flat=0, resolution=1024)), (5, AbsInfo(value=683, min=-2097152, max=2097152, fuzz=16, flat=0, resolution=1024))], 4: [5]}
2025-07-06 11:20:09 [INFO] - info bus: 0005, vendor 054c, product 09cc, version 8100
2025-07-06 11:20:09 [INFO] - phys 
2025-07-06 11:20:09 [INFO] - uniq XX:XX:XX:XX:XX:XX
2025-07-06 11:20:09 [INFO] - version 65537

2025-07-06 11:20:09 [INFO] /dev/input/event4 Wireless Controller Touchpad
2025-07-06 11:20:09 [INFO] - capabilities: {0: [0, 1, 3], 1: [272, 325, 330, 333], 3: [(0, AbsInfo(value=1735, min=0, max=1919, fuzz=0, flat=0, resolution=0)), (1, AbsInfo(value=367, min=0, max=941, fuzz=0, flat=0, resolution=0)), (47, AbsInfo(value=0, min=0, max=1, fuzz=0, flat=0, resolution=0)), (53, AbsInfo(value=0, min=0, max=1919, fuzz=0, flat=0, resolution=0)), (54, AbsInfo(value=0, min=0, max=941, fuzz=0, flat=0, resolution=0)), (57, AbsInfo(value=0, min=0, max=65535, fuzz=0, flat=0, resolution=0))]}
2025-07-06 11:20:09 [INFO] - info bus: 0005, vendor 054c, product 09cc, version 8100
2025-07-06 11:20:09 [INFO] - phys 
2025-07-06 11:20:09 [INFO] - uniq XX:XX:XX:XX:XX:XX
2025-07-06 11:20:09 [INFO] - version 65537
```


## 補足: 環境設定メモ

* evdev のインストールに以下が必要かも
  - `apt-get install gcc`: evdev ビルド時に gcc コンパイラが使われるため
  - `apt-get install python3-dev`: evdev ビルド時に Python.h を参照するため
