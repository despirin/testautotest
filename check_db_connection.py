import pymysql.cursors
from fixture.orm import ORMFixture

db = ORMFixture(host='localhost',
                             user='root',
                             password='',
                             name='addressbook')
try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))


    # groups = db.get_group_list()
    # for group in groups:
    #     print(group)
    # print(len(groups))



finally:
    db.destroy()






