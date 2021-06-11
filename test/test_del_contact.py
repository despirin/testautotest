# delete first contact from list


def test_del_contact(app):
    app.session.login("admin", "secret")
    app.contact.del_first()
    app.session.logout()

