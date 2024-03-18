import sqlite3

#fetchall
def fetchall(table):
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = ''

def fetchall_patient():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = ' select * from patient;'
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("ID  | name                | type   | disease             ")
    for patient in results:
        print(f"{patient[0]:<4}| {patient[1]:<20}| {patient[2]:<7}| {patient[3]:<20}")
    db.close
def fetchall_doner():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from doner;'
    cursor.execute(sql)
    results = cursor.fetchall()

    print("ID  | name                | type   | number         ")
    for doner in results:
        print(f"{doner[0]:<4}| {doner[1]:<20}| {doner[2]:<7}| {doner[3]}:<15")
    db.close
def fetchall_donation():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from donation;'
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("ID  | donerID | doner name          | date      | bankID")
    for donation in results:
        print(f"{donation[0]:<4}| {donation[1]:<8}| {donation[2]:<20}| {donation[3]:<9}| {donation[4]}")
    db.close
def fetchall_bank():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from bank;'
    cursor.execute(sql)
    results = cursor.fetchall()

    print("ID  | address")
    for bank in results:
        print(f"{bank[0]:<4}| {bank[1]}")
    db.close
def fetchall_usage():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from usage;'
    cursor.execute(sql)
    results = cursor.fetchall()

    print("ID  | pateintID | donerID | date")
    for usage in results:
        print(f"{usage[0]:<4}| {usage[1]:<10}| {usage[2]:<8}| {usage[3]}")
    db.close

#update
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

#add
def add():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    db.close

def delete(table, where, condition):
    db = sqlite3.connect('bloodbank_db')
    db.close


while True:

    print("""\nWelcome to Blood Bank Manage System\n
1. Tables:
2. Patient
3. Doner
4. Donation
5. Bank  
6. Usage
""")
    table = input("Type number for table you would like to view/alter: ")
    if table == "1": #patient
        function = input("Type 1 to view table, type 2 to make change: ")
        if function == "1":
            fetchall_patient()
            break
        elif function == "2":
            change = input("Type 1 to update, type 2 to add, or type 3 to delete a patient: ")
            if change == "1":
                column = input("Enter column: ")
                change = input("Enter value: ")
                where = input("Enter condition: ")      
                condition = input("Enter condition value: ") #how to get 2 values from one input statement
                update(table, column, change, where, condition)
                break
            # elif change == "2":
            # elif change == "3":