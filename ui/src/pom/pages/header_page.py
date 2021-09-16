import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.src.pom.locators import HeaderLocators
from ui.src.pom.pages.base_page import BasePage


class GdHeader(BasePage):

    @allure.step("Click on 'About' in header")
    def click_on_about(self):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, HeaderLocators.ABOUT_BUTTON)))
        about = self.driver.find_element_by_xpath(HeaderLocators.ABOUT_BUTTON)
        about.click()

    @allure.step("Click on 'get in touch' button")
    def click_get_in_touch(self):
        self.get_wait().until(EC.element_to_be_clickable((By.CSS_SELECTOR, HeaderLocators.GET_IN_TOUCH)))
        get_in_touch = self.driver.find_element_by_css_selector(HeaderLocators.GET_IN_TOUCH)
        get_in_touch.click()

