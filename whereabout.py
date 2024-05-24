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
	driver.get('file:///index.html')

	device = evdev.InputDevice('/dev/input/event6')
	
    flag = 0
    while True:
        try:
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                    if event.value == 0:
                    	if event.code == evdev.ecodes.KEY_KP1:
                    		driver.get('file:///home.html')
                    	if event.code == evdev.ecodes.KEY_KP2:
                    		driver.get('file:///labo.html')
                        if event.code == evdev.ecodes.KEY_KP3:
                    		driver.get('file:///meeting.html')
        except KeyboardInterrupt:
            break
