# methods for contacts
import time
import re

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

    def add_to_group(self, contact, group):
        wd = self.app.wd
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("to_group").click()
        for we_group in wd.find_elements_by_xpath("//select[@name='to_group']//option"):
            if we_group.get_attribute("value") == group.id:
                we_group.click()
        wd.find_element_by_name("add").click()
        # return
        self.open_home_page()

        self.contact_cache = None

    def remove_from_group(self, contact, group):
        wd = self.app.wd
        # выбрать группу из выпадающего списка
        for we_in_group in wd.find_elements_by_xpath("//select[@name='group']//option"):
            if we_in_group.get_attribute("value") == group.id:
                wd.find_element_by_name("group").click()
                we_in_group.click()
                break
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("remove").click()
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        time.sleep(15)
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # define record line
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@title='Edit']//parent::a[contains(@href,'id="+id+"')]").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        # define record line
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # define record line
        # wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        # return
        self.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        # self.select_contact_by_id(id)
        # wd.find_element_by_name("edit").click()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_data(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//form[@name='MainForm']")) == 1):
            #wd.find_element_by_xpath("//a[text()='home']").click()
            wd.find_element_by_xpath("//img[@title='Addressbook']").click()

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
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[2].text
                lname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                # here: we need additional check if we have some empty phones

                self.contact_cache.append(ContactInfo(firstname=name, lastname=lname, id=id,
                                                      all_phones_from_home_page=all_phones,
                                                      all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return ContactInfo(home=homephone, work=workphone,
                           mobile=mobilephone, phone2=secondaryphone,
                           firstname=firstname, lastname=lastname,
                           id=id, email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return ContactInfo(home=homephone, work=workphone,
                           mobile=mobilephone, phone2=secondaryphone)

    @staticmethod
    def get_contact_by_id_from_clist(contacts_list, c_id):
        cont = None
        for contact in contacts_list:
            if contact.id == c_id:
                cont = contact
        return cont
