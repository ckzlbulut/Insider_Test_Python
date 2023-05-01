import pytest


@pytest.mark.usefixtures("setup")
class Test_Insider:

    def test_homepage(self):
        self.driver.get('https://www.useinsider.com/')
        self.homepage.accept_cookies()
        self.homepage.assert_homepage_loaded()

    def test_career(self):
        self.homepage.click_more_menu()
        self.homepage.click_careers()

        self.career_page.assert_our_location_visible()
        self.career_page.assert_teams_visible()
        self.career_page.assert_insider_life_visible()

    def test_job_list(self):
        self.career_page.click_see_all_teams()
        self.career_page.click_quality_assurance()
        self.qa_page.click_see_all_qa_jobs()

        self.qa_page.select_location('Istanbul, Turkey')
        self.qa_page.assert_job_list_presence()

    def test_job_posts(self):
        self.qa_page.assert_positions_contains("quality assurance")
        self.qa_page.assert_departments_contains("quality assurance")
        self.qa_page.assert_locations_contains("Istanbul, Turkey")
        self.qa_page.assert_apply_button()

    def test_job_apply(self):
        self.qa_page.click_apply_buttons()

