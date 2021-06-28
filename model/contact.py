
class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None,
                 company=None, title=None, homephone=None, workphone=None,
                 mobilephone=None, secondaryphone=None, all_phone_from_homepage=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.title = title
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.allphone = all_phone_from_homepage


'''
firstname="test_firstname"
middlename="test_secondname",
lastname="test_lastname",
nickname="test_nickname", 
company="test_company", 
title="test_title" 
homephone="test_HomePhone",
workphone="Test_workphone",
mobilephone="test_mobilephone",
secondaryphone="test_secondary_phone"
'''