from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.title('Рузультатов поиска 10')
@allure.severity(Severity.BLOCKER)
def test_yandex():
    driver = WebDriver(executable_path='F://job//selenium//chromedriver.exe')
    with allure.step('Открываем страницу поиска'):
        driver.get('https://ya.ru')
    with allure.step('Идем на яндекс маркет'):
        search_input = driver.find_element_by_xpath('//input[@id="text"]')
        search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
        search_input.send_keys("market.yandex.ru")
        search_button.click()

    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) == 10
    with allure.step('Ожидаем, что колличесвто результатов станет 10'):

        WebDriverWait(driver, 10, 0.5).until(check_results_count)

    with allure.step('Переходим по ссылке первого результата'):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        link = search_results[0].find_element_by_xpath('.//h2/a')
        link.click()
    driver.switch_to_window(driver.window_handles[1])
    with allure.step('Проверяем корректность тайтла'):
        assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'
