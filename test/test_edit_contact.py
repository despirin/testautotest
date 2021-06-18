from model.contact import Contact
#
#
def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test_test_new"))
    app.contact.modify_first_contact("firstname","firstname_test_test")