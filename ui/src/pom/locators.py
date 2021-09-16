class HeaderLocators(object):
    ABOUT_BUTTON = "//a[text()=' About ']"
    GET_IN_TOUCH = ".contact-button"


class CompanyPageLocators(object):
    CEO_NAME = "//div[@class='gd-row gd-row-centered management-heads']//div[text()='Leonard Livschitz']"
    CEO_DESCRIPTION = ".description"


class BlogPageLocators(object):
    ARTICLE_FILTER = "typelist"
    TOPIC_FILTER = "topiclist"
    ARTICLE_LIST = "div#typelist span"
    ARTICLE_ELEMENT = ".card"
    FILTER_BY = "//b[text() = 'Filter by']"
    DIGITAL_TRANSFORMATION = "//a[text() = 'Digital Transformation']"


class ContactPageLocators(object):
    FIRST_NAME_FIELD = "//input[@placeholder = 'First name*']"
    LAST_NAME_FIELD = "//input[@placeholder = 'Last name*']"
    EMAIL_FIELD = "//input[@placeholder = 'E-mail*']"
    SELECTOR_SOURCE = "//gd-select-legacy[@placeholder = 'How did you hear about us?']"
    OPTION = "//gd-select-option-legacy"
    CHECKBOX_TERMS = "//div[@class='terms']//span"
    CHECKBOX_CONTACT = "//span[text()=' I allow Grid Dynamics to contact me. ']/preceding-sibling::span"
    CONTACT_BUTTON = "//button[@type='submit']"

