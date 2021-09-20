import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.src.pom.locators import CompanyPageLocators
from ui.src.pom.pages.base_page import BasePage


class GdCompanyPage(BasePage):

    @allure.step("Check page title is COmpany")
    def is_title_matches(self):
        return "Company" in self.driver.title

    @allure.step("Click on CEO name")
    def click_ceo_name(self):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, CompanyPageLocators.CEO_NAME)))
        ceo_name = self.driver.find_element_by_xpath(CompanyPageLocators.CEO_NAME)
        ceo_name.click()
        self.get_wait().until((EC.visibility_of_element_located((By.CSS_SELECTOR, CompanyPageLocators.CEO_DESCRIPTION))))

    @allure.step("Get description from modal")
    def get_description(self):
        return self.driver.find_element_by_css_selector(CompanyPageLocators.CEO_DESCRIPTION).text
