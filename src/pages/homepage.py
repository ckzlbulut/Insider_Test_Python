from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from src.pages.BasePage import BasePage


class HomePage(BasePage):
    CAREER_URL = 'https://useinsider.com/careers/'

    ACCEPT_COOKIES = (By.XPATH, "//*[text()='Accept All']")
    HOME_PAGE = (By.XPATH, "//body[contains(@class,'home page-template')]")
    MORE_MENU = (By.XPATH, "//*[text()='More']")
    CAREERS = (By.CSS_SELECTOR, "[href='https://useinsider.com/careers/']")

    def accept_cookies(self):
        self.wait_and_click(self.ACCEPT_COOKIES)

    def assert_homepage_loaded(self):
        home_page_element = self.wait_visibility(self.HOME_PAGE)

        assert home_page_element.is_displayed()

    def click_more_menu(self):
        self.wait_and_click(self.MORE_MENU)

    def click_careers(self):
        self.wait_and_click(self.CAREERS)

        assert self.driver.current_url == self.CAREER_URL
