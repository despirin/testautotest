from model.group import Group


class GroupHelper:
    group_cache = None
    def __init__(self, app):
        self.app = app


    def open_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_page()
        wd.find_element_by_name("new").click()
        #fill group form
        self.fill_group_form(group)
        #submit
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        #self.group_cache = None


    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def get_group_list(self):
        #if self.group_cache is None:
        wd = self.app.wd
        self.open_page()
        self.group_cache = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            self.group_cache.append(Group(name=text, id=id))
        return list (self.group_cache)


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_page()
        self.select_first_group()
        #open modif form
        wd.find_element_by_name("edit").click()
        #fill new form
        self.fill_group_form(new_group_data)
        #submit
        wd.find_element_by_name("update").click()
        #return
        self.return_to_group_page()
        self.group_cache = None


    def count (self):
        wd = self.app.wd
        self.open_page()
        return len (wd.find_elements_by_name("selected[]"))


    def del_first_group(self):
        self.del_group_by_index(0)


    def del_group_by_index(self, index):
        wd = self.app.wd
        self.open_page()
        self.select_group_by_index(index)
        # delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def del_group_by_id(self, id):
        wd = self.app.wd
        self.open_page()
        self.select_group_by_id(id)
        # delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None