from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--kiosk')
options.experimental_option('excludeSwitches', ['enable-automation'])
options.binary_location = ('/usr/bin/chromium-browser')
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://google.com')
