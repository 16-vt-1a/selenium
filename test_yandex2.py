from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import allure
import time


@allure.title('Картинки')
@allure.severity(Severity.BLOCKER)
def test_yandex2():
    driver = WebDriver(executable_path='F://job//selenium//chromedriver.exe')
    with allure.step('Открываем страницу поиска'):
        driver.get('https://yandex.ru')

    def check_img():
        with allure.step('Ищем ссылку на картинки'):
            try:
                search_img = driver.find_element_by_link_text('Картинки')
                search_img.click()
                return True
            except NoSuchElementException:
                print('Картинок нет!')
                return False
    check_img()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(5)
    url = driver.current_url
    url1 = "https://yandex.ru/images/"
    with allure.step('Проверяем ссылку'):
        if url == url1:
            print("Ссылки совпадают")
        else:
            print("Ссылки не совпадают")
    with allure.step('Открываем первую картинку'):
        search_img1 = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[1]/div')
        search_img1.click()
    url2 = driver.current_url

    def check_big_img():
        with allure.step('Проверяем открылась ли картинка'):
            try:
                search_big_img = driver.find_element_by_xpath('.//div/div[2]/div/div[1]/div/div/div/img')
                return True
            except NoSuchElementException:
                return False
    check_big_img()
    with allure.step('Переходим на следующую картинку'):
        search_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div')
        search_btn.click()
    with allure.step('Переходим обратно на первую картинку и проверяем осталась ли она прежней'):
        search_btn_bc = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]')
        search_btn_bc.click()
        url3 = driver.current_url
        if url2 == url3:
            print("Картинки одинаковые")
        else:
            print("Картинки разные")
