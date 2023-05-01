from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BasePage():
    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.actions = ActionChains(driver)

    def wait_and_click(self, locator):
        element = self.wait_clickable(locator)
        element.click()

    def wait_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        return element

    def wait_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def wait_list_visibility(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        element = self.driver.find_elements(*locator)
        return element

    def scroll_to_element(self, locator):
        element = self.wait_visibility(locator)
        self.actions.scroll_to_element(element).perform()
        return element

    def click_with_JS(self, locator):
        element = self.wait_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_with_JS(self, locator):
        element = self.wait_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_presence_of_options(self, select_element, option_locator):
        self.wait.until(lambda d: len(select_element.find_elements(*option_locator)) > 1)

    def get_new_window_handle(self, main_window, all_windows):
        return [window for window in all_windows if window != main_window][0]
