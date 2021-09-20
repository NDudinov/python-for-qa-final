import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.src.pom.locators import ContactPageLocators
from ui.src.pom.pages.base_page import BasePage


class ContactUsPage(BasePage):

    @allure.step("Check page title")
    def is_title_matches(self):
        return "Contact us" in self.driver.title

    @allure.step("Fill first name on form")
    def fill_first_name(self, fname):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.FIRST_NAME_FIELD)))
        first_name = self.driver.find_element_by_xpath(ContactPageLocators.FIRST_NAME_FIELD)
        first_name.send_keys(fname)

    @allure.step("Fill last name on form")
    def fill_last_name(self, lname):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.LAST_NAME_FIELD)))
        last_name = self.driver.find_element_by_xpath(ContactPageLocators.LAST_NAME_FIELD)
        last_name.send_keys(lname)

    @allure.step("Fill email on form")
    def fill_email(self, email):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.EMAIL_FIELD)))
        email_field = self.driver.find_element_by_xpath(ContactPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    @allure.step("Select from dropdown 'How have heard about us'")
    def select_how_hear(self, option):
        dropdown = self.driver.find_element_by_xpath(ContactPageLocators.SELECTOR_SOURCE)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView({behavior: \"smooth\", block: \"center\", inline: \"nearest\"})",
            dropdown)
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.SELECTOR_SOURCE)))
        dropdown = self.driver.find_element_by_xpath(ContactPageLocators.SELECTOR_SOURCE)
        time.sleep(3)
        dropdown.click()
        # find_by = self.driver.find_element_by_xpath(BlogPageLocators.FILTER_BY)
        options = self.driver.find_elements_by_xpath(ContactPageLocators.OPTION)
        for o in options:
            if o.text == option:
                o.click()
                break
            else:
                continue

    @allure.step("Check checkbox 'I agree about terms and read policy'")
    def select_checkbox_terms(self):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.CHECKBOX_TERMS)))
        checkbox = self.driver.find_element_by_xpath(ContactPageLocators.CHECKBOX_TERMS)
        checkbox.click()

    @allure.step("Check checkbox 'I agree to contact'")
    def select_checkbox_contact(self):
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, ContactPageLocators.CHECKBOX_CONTACT)))
        checkbox = self.driver.find_element_by_xpath(ContactPageLocators.CHECKBOX_CONTACT)
        checkbox.click()

    @allure.step("Check 'Contact' button state")
    def check_contact_button_state(self):
        button = self.driver.find_element_by_xpath(ContactPageLocators.CONTACT_BUTTON)
        return button.is_enabled()
