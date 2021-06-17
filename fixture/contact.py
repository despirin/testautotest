from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact()
        return len(wd.find_elements_by_name("selected[]"))

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact()
        wd.find_element_by_link_text("add new").click()
        # fill group form
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()

    def fill_contact_form(self, contact):
        # wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("phone2", contact.secondaryphone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first(self):
        wd = self.app.wd
        self.open_contact()
        wd.find_element_by_name("selected[]").click()
#        delete first group
#        wd.find_element_by_name("delete").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, field_name, new_contact_data):
        wd = self.app.wd
        self.open_contact()
        self.open_contact_to_edit_by_index(0)
        # open modif form
        # wd.find_element_by_name("edit").click()
        # #fill new form
        self.change_field_value(field_name, new_contact_data)
        # #submit
        wd.find_element_by_name("update").click()
        # #return
        self.open_contact()
        # self.group_cache = None

########################################################################################################################
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = ["", "", "", "", ""]
                all_phones = cells[5].text.splitlines()


                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], workphone=all_phones[1],
                       mobilephone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_form_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("vale")
        lastname = wd.find_element_by_name("lastname").get_attribute("vale")
        id = wd.find_element_by_name("id").get_attribute("vale")
        homephone = wd.find_element_by_name("home").get_attribute("vale")
        workphone = wd.find_element_by_name("work").get_attribute("vale")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("vale")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("vale")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
