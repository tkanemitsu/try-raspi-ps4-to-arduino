#include <SoftwareSerial.h>

// SoftwareSerial(RX, TX)
SoftwareSerial raspiSerial(2, 3);  // RX = D2, TX = D3（今回は送信しない）

void setup() {
  Serial.begin(9600);      // USBシリアルモニタ用
  raspiSerial.begin(750);  // Raspberry Pi からの受信用

  Serial.println("SoftwareSerial Ready");
}

void loop() {
  if (raspiSerial.available()) {
    int b = raspiSerial.read();  // 1バイト受信

    Serial.print("HEX=0x");
    if (b < 0x10) Serial.print('0');  // 1桁のとき0埋め
    Serial.print(b, HEX);
    Serial.print(" dec=");
    Serial.print(b);
    Serial.print(" chr=");
    Serial.write(b);
    Serial.println();
  }
}
