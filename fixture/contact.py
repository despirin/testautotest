
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, Contact):
        wd = self.app.wd
        self.open_add_contact()
        # Contact(firstname, middlename, lastname, nickname, company, title)
        # fill firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        # fill middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        # fill lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        # fill nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        # fill companyname
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        # fill Title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        # submit
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()



    def del_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
#        delete first group
#        wd.find_element_by_name("delete").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()