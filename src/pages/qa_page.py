import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as EC
from src.pages.BasePage import BasePage


class QA_Page(BasePage):
    QA_OPEN_POS_URL = 'https://useinsider.com/careers/open-positions/?department=qualityassurance'
    LEVER_FORM_URL = 'https://jobs.lever.co/useinsider'

    LOCATION_INFO = (By.CSS_SELECTOR, ".location-info .mb-0")
    SEE_ALL_QA = (By.XPATH, "//*[text() ='See all QA jobs']")
    FILTER_LOCATION = (By.CSS_SELECTOR, "[name ='filter-by-location']")
    POSITION_TITLE = (By.CSS_SELECTOR, '.position-title')
    POSITION_DEPARTMENT = (By.CSS_SELECTOR, '.position-department')
    POSITION_LOCATION = (By.CSS_SELECTOR, '.position-location')
    NO_JOB = (By.CSS_SELECTOR, '.no-job-result')
    JOB_LIST = (By.CSS_SELECTOR, '.position-list-item-wrapper')
    POSITION_FILTER = (By.CSS_SELECTOR, "#career-position-filter")
    OPTION = (By.CSS_SELECTOR, "option")
    APPLY_BUTTON = (By.XPATH, "//*[text()='Apply Now']")
    LEVER_APPLY_BUTTON = (By.XPATH, "//*[text()='Apply for this job']")

    def click_see_all_qa_jobs(self):
        self.wait_and_click(self.SEE_ALL_QA)
        assert self.driver.current_url == self.QA_OPEN_POS_URL

    def select_location(self, location):
        select_element = self.wait_clickable(self.FILTER_LOCATION)

        self.wait_presence_of_options(select_element, self.OPTION)
        select_element = Select(select_element)

        select_element.select_by_visible_text(location)
        self.scroll_with_JS(self.POSITION_FILTER)

    def assert_job_list_presence(self):
        job_list = self.wait_list_visibility(self.JOB_LIST)

        assert len(job_list) > 0

    def assert_positions_contains(self, position: str):
        job_list = self.wait_list_visibility(self.JOB_LIST)

        for job_post in job_list:
            position_element = job_post.find_element(*self.POSITION_TITLE)
            assert position.lower() in position_element.text.lower()

    def assert_departments_contains(self, department: str):
        job_list = self.wait_list_visibility(self.JOB_LIST)

        for job_post in job_list:
            department_element = job_post.find_element(*self.POSITION_DEPARTMENT)
            assert department.lower() in department_element.text.lower()

    def assert_locations_contains(self, location: str):
        job_list = self.wait_list_visibility(self.JOB_LIST)

        for job_post in job_list:
            location_element = job_post.find_element(*self.POSITION_LOCATION)
            assert location.lower() in location_element.text.lower()

    def assert_apply_button(self):
        job_list = self.wait_list_visibility(self.JOB_LIST)

        for job_post in job_list:
            self.actions.move_to_element(job_post).perform()

            apply_button = job_post.find_elements(*self.APPLY_BUTTON)
            assert len(apply_button) > 0

    def click_apply_buttons(self):
        job_list = self.wait_list_visibility(self.JOB_LIST)
        postion_page_window = self.driver.current_window_handle

        for job_post in job_list:
            self.actions.move_to_element(job_post).perform()

            apply_button = self.wait_clickable(self.APPLY_BUTTON)
            apply_button.click()

            new_window = self.get_new_window_handle(postion_page_window, self.driver.window_handles)
            self.driver.switch_to.window(new_window)

            assert self.LEVER_FORM_URL in self.driver.current_url
            assert self.wait_clickable(self.LEVER_APPLY_BUTTON)

            self.driver.close()
            self.driver.switch_to.window(postion_page_window)
