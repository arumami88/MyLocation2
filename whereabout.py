import datetime
import evdev
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':

	# Parameters
	chrome_binary_location = '/usr/bin/chromium-browser'
	chrome_webdriver_location = '/usr/bin/chromedriver'
	input_device = '/dev/input/event6'
	mylocation_path = 'file:///home/imamura/MyLocation/'
	offmode_start = 910
	offmode_end = 920
	default_webpage = mylocation_path + 'home.html'  # default
	offmode_webpage = mylocation_path + 'blank.html'  # blank
	key7_webpage = mylocation_path + 'room.html'  # in room
	key8_webpage = mylocation_path + 'lecture.html'  # lecture
	key9_webpage = mylocation_path + 'meeting.html'  # meeting
	key4_webpage = mylocation_path + 'labo.html'  # laboratory
	key5_webpage = mylocation_path + 'semi.html'  # seminar
	key6_webpage = mylocation_path + 'meal.html'  # meal
	key1_webpage = mylocation_path + 'univ.html'  # in univ.
	key2_webpage = mylocation_path + 'trip.html'  # business trip
	key3_webpage = mylocation_path + 'vacation.html'  # vacation
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

	offtime = 0  # 0: ON-mode, 1: OFF-mode
	location = 0  # default
	while True:
		try:
			for event in device.read_loop():
				# Obtaining of time information
				dt = datetime.datetime.now()
				ctime = 100 * dt.hour + dt.minute
				# Switching to OFF-mode by time
				if offtime == 0 and (ctime <= offmode_end or ctime >= offmode_start):
					offtime = 1
					driver.get(offmode_webpage)
				if offtime == 1 and (offmode_end < ctime < offmode_start):
					offtime = 0
					# === Costomize for keep location ===
					if location == 2:
						driver.get(key2_webpage)  # business trip
					elif location == 3:
						driver.get(key3_webpage)  # vacation
					else:
						driver.get(default_webpage)
					# ===================================

				if event.type == evdev.ecodes.EV_KEY:
					if event.value == 0:
						if event.code == evdev.ecodes.KEY_KP0:
							driver.get(key0_webpage)
							location = 0
						if event.code == evdev.ecodes.KEY_KP1:
							driver.get(key1_webpage)
							location = 1
						if event.code == evdev.ecodes.KEY_KP2:
							driver.get(key2_webpage)
							location = 2
						if event.code == evdev.ecodes.KEY_KP3:
							driver.get(key3_webpage)
							location = 3
						if event.code == evdev.ecodes.KEY_KP4:
							driver.get(key4_webpage)
							location = 4
						if event.code == evdev.ecodes.KEY_KP5:
							driver.get(key5_webpage)
							location = 5
						if event.code == evdev.ecodes.KEY_KP6:
							driver.get(key6_webpage)
							location = 6
						if event.code == evdev.ecodes.KEY_KP7:
							driver.get(key7_webpage)
							location = 7
						if event.code == evdev.ecodes.KEY_KP8:
							driver.get(key8_webpage)
							location = 8
						if event.code == evdev.ecodes.KEY_KP9:
							driver.get(key9_webpage)
							location = 9
		except KeyboardInterrupt:
			break
