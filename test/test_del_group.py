# -*- coding: utf-8 -*-

def test_del_first_group(app):
    app.session.login("admin", "secret")
    app.group.test_del_first_group()
    app.session.logout()
