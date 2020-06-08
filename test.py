from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def my_func():
    driver = webdriver.Chrome()
    driver.get('https://www.itau.com.br/')

    time.sleep(5)

    try:
        assert "Banco Itaú | Tudo pra você" in driver.title
        print("ok!")
        input_agencia = driver.find_element_by_id('agencia')
        input_agencia.click()
        input_agencia.send_keys(agencia)

        input_conta = driver.find_element_by_id('conta')
        input_conta.click()
        input_conta.send_keys(conta)
        

        actions = ActionChains(driver).send_keys(Keys.TAB)
        driver.find_element_by_id('btnLoginSubmit').click()

        time.sleep(5)
        
        a = driver.find_element(By.XPATH, '//a[text()="1 ou 3"]')
        print(a)

        time.sleep(10)
        # driver.close()

    except AssertionError:
        print("error!")


if __name__ == "__main__":
    my_func()
