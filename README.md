# ラズベリーパイを使ったデジタル所在表



## 使用機器

| 種類 | 名称 |
| --- | --- |
| マイコン | Raspberry Pi 3 Model B+ |
| ディスプレイ | Kumen 3.5インチモニタ（GPIO, 480x329）|
| 入力機器 | 無線テンキー（2.4G Hz）|

| 種類 | 名称 |
| --- | --- |
| マイコン | Raspberry Pi 3 Model B+ |
| ディスプレイ | Dodomi 10.1インチモニタ（HDMI,1290×800）|


## 1. Raspberry Pi 3 のOSインストールと初期設定

- [公式ページ](https://www.raspberrypi.com/software/) から **Raspberry Pi Imager** をダウンロードしてPCにインストール。

- Raspberry Pi Imagerを起動して，MicroSD カードにOSを書き込む。**Raspberry Pi OS (Legacy, 32-bit)** を選択。

- Raspberry Pi に MicroSD を差し込み，起動して初期設定。**Wi-Fiの設定** をして **ソフトウェアの更新** をして再起動。

## 2. Kuman 3.5インチLCDの設定

- LDC-show をインストール（※goodtft版は動作せず）

    git clone https://github.com/waveshare/LCD-show.git
    chmod -R 755 LCD-show
    cd LCD-show
    ./LCD35-show

　実行すると自動的に再起動して3.5インチLCD表示に切り替わる。