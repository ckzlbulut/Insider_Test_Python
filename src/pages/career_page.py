from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage


class CareerPage(BasePage):
    QA_PAGE_URL = 'https://useinsider.com/careers/quality-assurance/'

    OUR_LOCATION = (By.CSS_SELECTOR, "#career-our-location")
    LIFE_INSIDER = (By.CSS_SELECTOR, "[data-id='a8e7b90']")
    SEE_ALL_TEAMS = (By.XPATH, "//*[text() ='See all teams']")
    TEAMS = (By.CSS_SELECTOR, "#career-find-our-calling")
    QUALITY_ASSURANCE = (By.CSS_SELECTOR, "[href = 'https://useinsider.com/careers/quality-assurance/']")

    def assert_our_location_visible(self):
        our_location = self.wait_visibility(self.OUR_LOCATION)

        assert our_location.is_displayed()

    def assert_teams_visible(self):
        teams = self.wait_visibility(self.TEAMS)

        assert teams.is_displayed()

    def assert_insider_life_visible(self):
        life_insider = self.wait_visibility(self.LIFE_INSIDER)

        assert life_insider.is_displayed()

    def click_see_all_teams(self):
        self.click_with_JS(self.SEE_ALL_TEAMS)

    def click_quality_assurance(self):
        self.click_with_JS(self.QUALITY_ASSURANCE)

        assert self.driver.current_url == self.QA_PAGE_URL
