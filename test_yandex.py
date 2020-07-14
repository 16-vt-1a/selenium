from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import allure
import time


@allure.title('Поиск')
@allure.severity(Severity.BLOCKER)
def test_yandex():
    driver = WebDriver(executable_path='F://job//selenium//chromedriver.exe')
    j = 1
    while j < 6:
        index = str(j)
        with allure.step('Открываем страницу поиска'):
            driver.get('https://ya.ru')
        with allure.step('Ищем Тензор'):
            search_input = driver.find_element_by_xpath('//input[@id="text"]')
            search_input.send_keys("Тензор")

        def check_exists(driver):
            result = driver.find_elements_by_xpath('//span[@class="suggest2-item__text"]')
            return len(result) > 1

        with allure.step('Ожидаем, что количество подсказок больше 1'):

            WebDriverWait(driver, 10, 0.5).until(check_exists)
        with allure.step('Выбираем элемент подсказки'):
            search_results = driver.find_elements_by_xpath('//li[@class="suggest2-item i-bem suggest2-item_js_inited"]')
            link = driver.find_element_by_xpath('.//li[' + index + ']')
            link.click()

        def check_results_count(driver):
            inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
            return len(inner_search_results) >= 10

        with allure.step('Ожидаем, что количесвто результатов поиска станет 10 и больше'):

            WebDriverWait(driver, 10, 0.5).until(check_results_count)

        def check_by_xpath():
            with allure.step('Ищем ссылку на tensor.ru'):
                try:
                    elem = driver.find_element_by_partial_link_text("tensor.ru")
                    return True
                except NoSuchElementException:
                    print('Zero element!')
                    return False
        check_by_xpath()
        j += 1
