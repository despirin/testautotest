# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    # test_contact = Contact(firstname="test_firstname",
    #                        middlename="test_secondname",
    #                        lastname="test_lastname",
    #                        nickname="test_nickname",
    #                        company="test_company",
    #                        title="test_title",
    #                        homephone="test_HomePhone",
    #                        workphone="Test_workphone",
    #                        mobilephone="test_mobilephone",
    #                        secondaryphone="test_secondary_phone")
    #app.contact.create_contact(test_contact)
    app.contact.create_contact(Contact(firstname="test_firstname", middlename="test_secondname",
                           lastname="test_lastname",
                           nickname="test_nickname",
                           company="test_company",
                           title="test_title",
                           homephone="test_HomePhone",
                           workphone="Test_workphone",
                           mobilephone="test_mobilephone",
                           secondaryphone="test_secondary_phone"))
