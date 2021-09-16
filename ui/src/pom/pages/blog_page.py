import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.src.pom.locators import BlogPageLocators
from ui.src.pom.pages.base_page import BasePage


class GdBlogPage(BasePage):

    @allure.step("Check page title is Grid Dynamics Blog")
    def is_title_matches(self):
        return "Grid Dynamics Blog" in self.driver.title

    @allure.step("Check article filter is available")
    def is_article_filter_available(self):
        filter_article_dropdown = self.driver.find_element_by_id(BlogPageLocators.ARTICLE_FILTER)
        if filter_article_dropdown.is_enabled:
            return True
        else:
            return False

    @allure.step("Check topic filter is clickable")
    def is_topic_filter_clickable(self):
        filter_topic_dropdown = self.driver.find_element_by_id(BlogPageLocators.TOPIC_FILTER)
        return filter_topic_dropdown.is_clickable

    @allure.step("Click article filter")
    def click_article_filter(self):
        filter_by = self.driver.find_element_by_xpath(BlogPageLocators.FILTER_BY)
        self.driver.execute_script("return arguments[0].scrollIntoView({behavior: \"smooth\", block: \"center\", inline: \"nearest\"})", filter_by)
        self.get_wait().until(EC.element_to_be_clickable((By.XPATH, BlogPageLocators.FILTER_BY)))
        filter_article_dropdown = self.driver.find_element_by_id(BlogPageLocators.ARTICLE_FILTER)
        self.get_wait().until(EC.element_to_be_clickable((By.ID, BlogPageLocators.ARTICLE_FILTER)))
        time.sleep(3) # couldn't find another way to do it.
        filter_article_dropdown.click()

    @allure.step("Select article type")
    def select_article_type(self, article_type):
        self.get_wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR, BlogPageLocators.ARTICLE_LIST)))
        # find_by = self.driver.find_element_by_xpath(BlogPageLocators.FILTER_BY)
        articles_types = self.driver.find_elements_by_css_selector(BlogPageLocators.ARTICLE_LIST)
        for a in articles_types:
            if a.text == article_type:
                a.click()
                break
            else:
                continue

    @allure.step("Get amount of result articles")
    def get_amount_of_articles(self):
        self.get_wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR, BlogPageLocators.ARTICLE_ELEMENT)))
        articles_types = self.driver.find_elements_by_css_selector(BlogPageLocators.ARTICLE_ELEMENT)
        return len(articles_types)



