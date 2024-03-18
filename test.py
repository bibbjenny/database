# name = "Jenny"
# type_ = "A"
# new_name = input("enter name: {name}")

# #

# import sqlite3
# db = sqlite3.connect('bloodbank_db')
# cursor = db.cursor()
# sql = ' select * from patient;'
# cursor.execute(sql)
# results = cursor.fetchall()
# print(results)

import sqlite3

def update_patient(new_name, new_type, new_disease, where, condition): #main loop add 'if no:'
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = '''update patient
    set name = ?, type = ?, disease = ?
    where ? = ?;'''
    values = (new_name, new_type, new_disease, where, condition)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    print("Table has been updated.")

update_patient("John Smith", "O", "cancer", "ID", "1")