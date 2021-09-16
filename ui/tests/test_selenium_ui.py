import allure
import pytest
from chromedriver_py import binary_path
from hamcrest import assert_that
from hamcrest import is_
from hamcrest.library.text.stringcontains import contains_string
from selenium import webdriver

from ui.src.pom.pages.blog_page import GdBlogPage
from ui.src.pom.pages.company_page import GdCompanyPage
from ui.src.pom.pages.contact_page import ContactUsPage
from ui.src.pom.pages.header_page import GdHeader

driver = webdriver.Chrome(executable_path=binary_path)


@pytest.fixture(scope="class")
def driver_open():
    driver.maximize_window()
    driver.set_page_load_timeout(20)
    yield "Clear up"
    driver.quit()


class TestGridBlog(object):
    @allure.title("Check info about Leonard")
    def test_about_ceo(self, driver_open):
        driver.get("https://blog.griddynamics.com")
        header_page = GdHeader(driver)
        header_page.click_on_about()
        company_page = GdCompanyPage(driver)
        company_page.is_title_matches()
        company_page.click_ceo_name()
        ceo_description = company_page.get_description()
        check_line = "director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014"
        assert_that(ceo_description, contains_string(check_line))

    @allure.title("Check article filter")
    def test_article_filter(self, driver_open):
        driver.get("https://blog.griddynamics.com")
        article_page = GdBlogPage(driver)
        assert_that(article_page.is_article_filter_available(), is_(True))
        article_page.click_article_filter()
        article_page.select_article_type("White Papers")
        white_papers_list_size = article_page.get_amount_of_articles()
        article_page.click_article_filter()
        article_page.select_article_type("Articles")
        articles_list_size = article_page.get_amount_of_articles()
        assert_that(articles_list_size > white_papers_list_size, is_(True))

    @allure.title("Check contact us form")
    def test_contact_us(self, driver_open):
        driver.get("https://blog.griddynamics.com")
        header_page = GdHeader(driver)
        header_page.click_get_in_touch()
        contact_page = ContactUsPage(driver)
        contact_page.fill_first_name("Anna")
        contact_page.fill_last_name("Smith")
        contact_page.fill_email("annasmith@griddynamics.com")
        contact_page.select_how_hear("Online Ads")
        contact_page.select_checkbox_terms()
        contact_page.select_checkbox_contact()
        assert_that(contact_page.check_contact_button_state(), is_(False))
