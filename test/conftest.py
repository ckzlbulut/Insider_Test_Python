import pytest
from selenium import webdriver

from src.pages.career_page import CareerPage
from src.pages.homepage import HomePage
from src.pages.qa_page import QA_Page


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Page Object Dosyalarının örneklerini oluştur
    homepage = HomePage(driver)
    career_page = CareerPage(driver)
    qa_page = QA_Page(driver)

    # request.cls ile sınıf örneği oluşturulur ve her sayfa örneği bu sınıfın bir özelliği haline getirilir
    request.cls.driver = driver
    request.cls.homepage = homepage
    request.cls.career_page = career_page
    request.cls.qa_page = qa_page

    yield

    driver.quit()