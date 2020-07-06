
import datetime
import os
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = "C:\\Program Files (x86)\\Google\\Chrome\\chromedriver\\"

# definicoes para rodar o chromedriver em modo "headless" ('browser oculto')
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_driver = CHROMEDRIVER_PATH + "chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options,
                          executable_path=chrome_driver)

url = 'https://github.com/alexandremot'


def get_screenshot():
    my_dir = os.chdir('C:\\programming\\python-selenium\\screenshots')
    timestamp = (datetime.datetime.now()).strftime('%H%M%S.%f')
    driver.save_screenshot('screenshot_' + timestamp + '.png')


def my_func():
    driver.get(url)
    get_screenshot()
    time.sleep(2)
    driver.close


if __name__ == "__main__":
    for i in range(2):
        x = threading.Thread(target=my_func, args=())
        x.start()
