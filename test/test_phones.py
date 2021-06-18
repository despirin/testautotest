
# def test_phones_on_homepage (app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_form_edit_page(0)
#     assert contact_from_home_page.all_phone_from_homepage == merge_mobile_phone(contact_from_edit_page)



def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_form_edit_page(0)
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_home_page.secondaryphone == contact_from_edit_page.secondaryphone

def merge_mobile_phone(contact):
    return "\n".join([contact.homephone,contact.workphone,contact.mobilephone,contact.secondaryphone])