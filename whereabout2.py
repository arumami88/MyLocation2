import subprocess
import evdev
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':

	# Parameters
	chrome_binary_location = '/usr/bin/chromium-browser'
	chrome_webdriver_location = '/usr/bin/chromedriver'
	input_device = '/dev/input/event0'
	mylocation_path = 'file:///home/imamura/MyLocation/'
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

	while True:
		try:
			for event in device.read_loop():
				if event.type == evdev.ecodes.EV_KEY:
					if event.code == evdev.ecodes.KEY_KP0:
						driver.get(key0_webpage)
						subprocess.call(['cp /home/imamura/www/home.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP1:
						driver.get(key1_webpage)
						subprocess.call(['cp /home/imamura/www/univ.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP2:
						driver.get(key2_webpage)
						subprocess.call(['cp /home/imamura/www/trip.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP3:
						driver.get(key3_webpage)
						subprocess.call(['cp /home/imamura/www/vacation.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP4:
						driver.get(key4_webpage)
						subprocess.call(['cp /home/imamura/www/labo.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP5:
						driver.get(key5_webpage)
						subprocess.call(['cp /home/imamura/www/semi.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP6:
						driver.get(key6_webpage)
						subprocess.call(['cp /home/imamura/www/meal.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP7:
						driver.get(key7_webpage)
						subprocess.call(['cp /home/imamura/www/room.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP8:
						driver.get(key8_webpage)
						subprocess.call(['cp /home/imamura/www/lecture.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KP9:
						driver.get(key9_webpage)
						subprocess.call(['cp /home/imamura/www/meeting.html /home/imamura/www/index.html'], shell=True)
					if event.code == evdev.ecodes.KEY_KPENTER:
						driver.get(offmode_webpage)
						subprocess.call(['cp /home/imamura/www/home.html /home/imamura/www/index.html'], shell=True)
		except KeyboardInterrupt:
			break
