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
```
cd ~
git clone https://github.com/waveshare/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show
./LCD35-show
```
実行すると自動的に再起動して3.5インチLCD表示に切り替わる。

- HDMI表示に戻すには下記コマンドを実行する。
```
cd ~/LCD-show
./LCD-hdmi
```
ある程度の作業が完了するまで，大画面のHDMIディスプレイで作業する方が楽。

## 3. 表示切替用キーの設定

- テンキーを接続して，デバイスの確認。
```
cat /proc/bus/input/devices
```
下記のコマンドで接続前後の差分を確認してもよい。増えたものが接続デバイス。
```
ls /dev/input
```

- evdev のインストールと動作確認
```
sudo pip3 install evdev
```
### 動作確認用のサンプルコード（接続デバイスが /dev/input/event0 の例）[buttontest.py](buttontest.py)
```
import evdev

device = evdev.InputDevice('/dev/input/event0')
for event in device.read_loop():
	if event.type == evdev.ecodes.EV_KEY:
		if event.value == 0:
			print(event.code, evdev.ecodes.KEY[event.code])
```
表示と関連付けるキーコード番号とコード名を確認しておく。

## 4. Chromium の自動操作（Selenium）の設定

- selenium のインストール
```
pip install selenium
```

- Chromium のドライバをインストール
```
sudo apt install chromium-chromedriver
```

- ドライバのパスを確認（特に設定を変更していなければ /usr/bin/chromedriver）
```
which chromedriver
```
- Chromium のアップデート
```
sudo apt-get dist-upgrade chromium-browser
```

### 動作確認用のサンプルコード（KioskモードによるChrome起動と google ページの表示）[chrometest.py](chrometest.py)
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--kiosk')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.binary_location = ('/usr/bin/chromium-browser')
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://google.com')
```