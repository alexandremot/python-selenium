
import datetime
import os
import threading
import time
from selenium import webdriver


url = 'https://github.com/alexandremot'
driver = webdriver.Chrome()


def get_screenshot():
    my_dir = os.chdir('C:\\programming\\python-selenium\\screenshots')
    timestamp = (datetime.datetime.now()).strftime('%H%M%S.%f')
    driver.save_screenshot('screenshot' + timestamp + '.png')


def my_func():
    driver.get(url)
    get_screenshot()
    time.sleep(2)
    driver.close


if __name__ == "__main__":
    for i in range(2):
        x = threading.Thread(target=my_func, args=())
        x.start()
