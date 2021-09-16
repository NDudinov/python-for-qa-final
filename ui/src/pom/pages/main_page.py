from base_page import BasePage


class GdMainPage(BasePage):

    def is_title_matches(self):
        return "Grid Dynamics: digital transformation at enterprise scale" in self.driver.title
