# methods for contacts
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.contact import ContactInfo


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_contact_form(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php")):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # open
        self.open_new_contact_form()
        self.fill_contact_data(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return
        self.open_home_page()
        self.contact_cache = None

    def fill_contact_data(self, contact):
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home)
        self.app.change_field_value("mobile", contact.mobile)
        self.app.change_field_value("work", contact.work)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)
        self.app.change_select_value("bday", contact.bday)
        self.app.change_select_value("bmonth", contact.bmonth)
        self.app.change_field_value("byear", contact.byear)
        self.app.change_select_value("aday", contact.aday)
        self.app.change_select_value("amonth", contact.amonth)
        self.app.change_field_value("ayear", contact.ayear)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact record
        wd.find_elements_by_name("selected[]")[index].click()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # workaround. Because after accept alertbox for some milisec displayed list of contacts without changes,
        # then msgbox. So in this phase we get incorrect list of contacts (get_contact_list()). time.sleep() - bad
        # practice
        time.sleep(1)
        # wait = WebDriverWait(wd, 10)
        # wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='msgbox']")))
        self.open_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # define record line
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        # return
        self.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//form[@name='MainForm']")) == 1):
            wd.find_element_by_xpath("//a[text()='home']").click()

    def amount(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")) - 1

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                name = element.find_element_by_xpath(".//td[3]").text
                lname = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(ContactInfo(firstname=name, lastname=lname, id=id))
            return list(self.contact_cache)
