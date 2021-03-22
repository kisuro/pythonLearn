# methods for groups

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (self.is_group_page()):
            wd.find_element_by_link_text("groups").click()

    def is_group_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # new
        wd.find_element_by_name("new").click()
        self.fill_group_data(group)
        # submit
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_data(self, group):
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        #
        self.fill_group_data(new_group_data)
        #
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (self.is_group_page()):
            wd.find_element_by_link_text("group page").click()

    def amount(self):
        wd = self.app.wd
        self.open_groups_page()
        # define form
        group_form = wd.find_element_by_xpath("//div[@id='content']//form")
        # get amount of group form elements
        amount_elements_in_form = len(group_form.find_elements_by_xpath(".//*"))
        # amount of elements for empty form is 8
        # each new record that +3el : 11 /14 /etc
        return int((amount_elements_in_form - 8) / 3)

    group_cache = None

    # метод для получения списка групп с UI (альтернатива получение данных списка прямо из БД: fixture/db.py -
    # get_group_list)
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
