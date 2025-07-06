# Raspi + Arduino 連携



## PS4ワイヤレスコントローラーの入力を受け取るサンプル (Python)

ソースコードや実行方法: [raspi_py_ps4_recv/](./raspi_py_ps4_recv/README.md)

### Raspiへのソースコード転送例

```sh
# サブディレクトリ raspi_py_ps4_recv のアーカイブ (.tar.gz) を作成
git archive --format=tar.gz --output=project.tar.gz HEAD raspi_py_ps4_recv

# Raspiにアーカイブを転送
scp project.tar.gz username@remote-host:/path/to/destination/

# Raspi上でアーカイブを展開し、実行
ssh username@remote-host
cd /path/to/destination
tar -xzf project.tar.gz

cd raspi_py_ps4_recv/
```


## PS4ワイヤレスコントローラーの入力を受け取るサンプル (C++)

WIP


## Raspi から Arduino を UART で制御するサンプル

WIP





## (参考) Raspberry Pi に PS4ワイヤレスコントローラー を Bluetooth ペアリングする方法

### 1. Raspberry Pi の Bluetooth を有効化

```sh
# bluetoothが有効化されているか確認 (既に enable なら OK)
systemctl status bluetooth

# bluetoothが有効化されていない場合、以下コマンドで有効化
sudo systemctl enable --now bluetooth
```

### 2. PS4コントローラーをペアリングモードにする

[SHARE] + [PS] ボタンを同時に長押し（ライトバーが白く点滅する）

### 3. `bluetoothctl` で接続

```sh
bluetoothctl
```

プロンプトが出たら以下を順に入力：

```
agent on
default-agent
scan on
```

ライトバーが点滅しているコントローラが表示されるまで待ちます。
例：

```
[NEW] Device XX:XX:XX:XX:XX:XX Wireless Controller
```

次に：

```
pair XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
```

成功したら scan off して exit します。

### 4. 接続確認

```sh
sudo apt install joystick
jstest /dev/input/js0
```

### トラブルシューティング

| 症状             | 対策                                                   |
| :--------------- | :----------------------------------------------------- |
| js0 が存在しない | `uinput` が読み込まれていない → `sudo modprobe uinput` |
