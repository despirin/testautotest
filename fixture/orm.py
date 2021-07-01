from pony.orm import *
from datetime import datetime


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional (str, colunm="group_name")
        header = Optional (str, colunm="group_header")
        footer = Optional(str, colunm="group_footer")

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='group_id')
        firstname = Optional (str, colunm="firstname")
        lastname  = Optional (str, colunm="lastname")
        deprecated = Optional(datetime, colunm='deprecated')

    def __init__ (self, host, name, user, password):
        self.db.bind ('mysql', host=host,
                             user=user,
                             password=password,
                             database=name)
        self.db.generate_mapping()


    def get_group_list(self):
        list(select(g for g in ORMFixture.ORMGroup))