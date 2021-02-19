# main fixture class (init driver/helpers)

from selenium import webdriver
from selenium.webdriver.support.select import Select

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        # init driver
        self.wd = webdriver.Firefox(executable_path='C:/ffdriver/geckodriver.exe')
        self.wd.implicitly_wait(30)
        # init our helpers
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        # close driver
        self.wd.quit()

    # navigation method(s)
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, select_name, select_value):
        wd = self.wd
        if select_value is not None:
            wd.find_element_by_name(select_name).click()
            Select(wd.find_element_by_name(select_name)).select_by_visible_text(select_value)
            wd.find_element_by_xpath("//option[@value='" + select_value + "']").click()
