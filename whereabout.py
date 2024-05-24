import datetime
import evdev
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':
	options = Options()
	options.add_argument('--kiosk')
	options.add_experimental_option('excludeSwitches', ['enable-automation'])
	options.binary_location = ('/usr/bin/chromium-browser')
	service = Service('/usr/bin/chromedriver')
	driver = webdriver.Chrome(options=options, service=service)
	driver.get('file:///home/imamura/arumami88/MyLocation/index.html')

	device = evdev.InputDevice('/dev/input/event6')

	flag = 0
	while True:
		try:
			for event in device.read_loop():
				dt = datetime.datetime.now()
				if dt.hour < 6:
					flag = 1
				else:
					flag = 0
				if flag == 0 and event.type == evdev.ecodes.EV_KEY:
					if event.value == 0:
						if event.code == evdev.ecodes.KEY_KP7:  # 在室
							driver.get('file:///home/imamura/arumami88/MyLocation/room.html')
						if event.code == evdev.ecodes.KEY_KP8:  # 講義
							driver.get('file:///home/imamura/arumami88/MyLocation/lecture.html')
						if event.code == evdev.ecodes.KEY_KP9:  # 会議
							driver.get('file:///home/imamura/arumami88/MyLocation/meeting.html')
						if event.code == evdev.ecodes.KEY_KP4:  # 研究室
							driver.get('file:///home/imamura/arumami88/MyLocation/home.html')
						if event.code == evdev.ecodes.KEY_KP5:  # ゼミ室
							driver.get('file:///home/imamura/arumami88/MyLocation/semi.html')
						if event.code == evdev.ecodes.KEY_KP6:  # 食事
							driver.get('file:///home/imamura/arumami88/MyLocation/meal.html')
						if event.code == evdev.ecodes.KEY_KP1:  # 学内
							driver.get('file:///home/imamura/arumami88/MyLocation/univ.html')
						if event.code == evdev.ecodes.KEY_KP2:  # 出張
							driver.get('file:///home/imamura/arumami88/MyLocation/trip.html')
						if event.code == evdev.ecodes.KEY_KP3:  # 休暇
							driver.get('file:///home/imamura/arumami88/MyLocation/vacation.html')
						if event.code == evdev.ecodes.KEY_KP0:  # 帰宅
							driver.get('file:///home/imamura/arumami88/MyLocation/home.html')
		except KeyboardInterrupt:
			break
