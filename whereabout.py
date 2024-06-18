import evdev
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':

	# Parameters
	chrome_binary_location = '/usr/bin/chromium-browser'
	chrome_webdriver_location = '/usr/bin/chromedriver'
	input_device = '/dev/input/event0'
	mylocation_path = 'file:///home/arumami88/MyLocation/html/'
	default_webpage = mylocation_path + 'home.html'  # default
	offmode_webpage = mylocation_path + 'blank.html'  # blank
	key9_webpage = mylocation_path + 'meal.html'  # meal
	key8_webpage = mylocation_path + 'blank.html'
	key7_webpage = mylocation_path + 'room.html'  # in room
	key6_webpage = mylocation_path + 'meeting.html'  # meeting
	key5_webpage = mylocation_path + 'blank.html'
	key4_webpage = mylocation_path + 'afk.html'  # afk
	key3_webpage = mylocation_path + 'trip.html'  # business trip
	key2_webpage = mylocation_path + 'blank.html'
	key1_webpage = mylocation_path + 'vacation.html'  # vacation
	key0_webpage = mylocation_path + 'home.html'  # home

	# Chromium setting for kiosk mode & automation
	options = Options()
	options.add_argument('--kiosk')
	options.add_experimental_option('excludeSwitches', ['enable-automation'])
	options.binary_location = chrome_binary_location
	service = Service(chrome_webdriver_location)
	driver = webdriver.Chrome(options=options, service=service)
	driver.get(default_webpage)

	# Setting of Input device
	device = evdev.InputDevice(input_device)

	while True:
		try:
			for event in device.read_loop():
				if event.type == evdev.ecodes.EV_KEY:
					if event.code == evdev.ecodes.KEY_KP0:
						driver.get(key0_webpage)
					if event.code == evdev.ecodes.KEY_KP1:
						driver.get(key1_webpage)
					if event.code == evdev.ecodes.KEY_KP2:
						driver.get(key2_webpage)
					if event.code == evdev.ecodes.KEY_KP3:
						driver.get(key3_webpage)
					if event.code == evdev.ecodes.KEY_KP4:
						driver.get(key4_webpage)
					if event.code == evdev.ecodes.KEY_KP5:
						driver.get(key5_webpage)
					if event.code == evdev.ecodes.KEY_KP6:
						driver.get(key6_webpage)
					if event.code == evdev.ecodes.KEY_KP7:
						driver.get(key7_webpage)
					if event.code == evdev.ecodes.KEY_KP8:
						driver.get(key8_webpage)
					if event.code == evdev.ecodes.KEY_KP9:
						driver.get(key9_webpage)
					if event.code == evdev.ecodes.KEY_KPENTER:
						driver.get(offmode_webpage)
		except KeyboardInterrupt:
			break
