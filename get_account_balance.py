
import datetime
import os
import threading
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
# snippet para rodar o selenium no modo headless
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
'''

load_dotenv()

dados_conta = {'agencia': os.getenv("AGENCIA"), 'conta': os.getenv("CONTA")}
senha = os.getenv("SENHA")


def get_screenshot(my_driver):
    my_dir = os.chdir('C:\\programming\\python-selenium\\screenshots')
    timestamp = (datetime.datetime.now()).strftime('%H%M%S.%f')
    my_driver.save_screenshot('screenshot' + timestamp + '.png')


def my_func():
    driver = webdriver.Chrome()
    driver.get('https://www.itau.com.br/')

    time.sleep(5)

    try:
        assert "Banco Itaú | Tudo pra você" in driver.title
        print("ok!")

        for dado in dados_conta.keys():
            text_box_input = driver.find_element_by_id(dado)
            text_box_input.click()
            text_box_input.send_keys(dados_conta[dado])

        time.sleep(1)

        actions = ActionChains(driver).send_keys(Keys.TAB)
        driver.find_element_by_id('btnLoginSubmit').click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '//div[@class="teclado clearfix"]'))
            )

        for item in senha:
            a = driver.find_element(By.XPATH,
                                    '//a[contains(text(), "' + item + '")]')
            a.click()
            #time.sleep(1)

        driver.find_element_by_id('acessar').click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//a[@class="warningView"]'))
            )

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        quadro_saldo = driver.find_element_by_id('tabSaldoExtratoDaConta')

        print(quadro_saldo.text)

        get_screenshot(driver)

    except AssertionError:
        print("error!")


if __name__ == "__main__":
    x = threading.Thread(target=my_func, args=())
    x.start()
    time.sleep(10)
    y = threading.Thread(target=my_func, args=())
    y.start()
