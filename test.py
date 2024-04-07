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

#add
def add_patient(new_name, new_btype, new_disease): #doesnt add
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"insert into Patient (name, type, disease) values ('{new_name}','{new_btype}','{new_disease}');"
    cursor.execute(sql)
    db.commit
    db.close()
    print("New patient has been successfully added.")

add_patient("Madison Simpson", "B+", "Allergies")