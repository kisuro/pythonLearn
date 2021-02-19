# methods for contacts

from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # open
        self.open_new_contact_form()
        self.fill_contact_data(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return
        self.return_to_home_page()

    def fill_contact_data(self, contact):
        wd = self.app.wd

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
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        # return
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def amount(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")) - 1
