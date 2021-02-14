# main fixture class (init driver/helpers)

from selenium import webdriver
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
