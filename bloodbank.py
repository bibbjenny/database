import sqlite3

def not_valid_num():
    print("It isn't a valid value. Please type a correct number.")

def fetch_one(table, column, id):
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"select {column} from {table} where id = {id} ;"
    cursor.execute(sql)
    results = cursor.fetchone()
    db.close()
    return results

def fetchall_patient():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = ' select * from patient;'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
def printall_patient(results): 
    print("ID  | name                | type   | disease             ")
    for patient in results:
        print(f"{patient[0]:<4}| {patient[1]:<20}| {patient[2]:<7}| {patient[3]:<20}")


def fetchall_doner():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from doner;'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
def printall_doner(results):
    print("ID  | name                | type   | number         ")
    for doner in results:
        print(f"{doner[0]:<4}| {doner[1]:<20}| {doner[2]:<7}| {doner[3]}:<15")

def fetchall_donation():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from donation;'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close
    return results
def printall_donation(results):
    print("ID  | donerID | doner name          | date      | bankID")
    for donation in results:
        print(f"{donation[0]:<4}| {donation[1]:<8}| {donation[2]:<20}| {donation[3]:<9}| {donation[4]}")

def fetchall_bank():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from bank;'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close
    return results
def printall_bank(results):
    print("ID  | address")
    for bank in results:
        print(f"{bank[0]:<4}| {bank[1]}")

def fetchall_usage():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from usage;'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close
    return results
def printall_usage(results):
    print("ID  | pateintID | donerID | date")
    for usage in results:
        print(f"{usage[0]:<4}| {usage[1]:<10}| {usage[2]:<8}| {usage[3]}")


#update
def update_patient(new_name, new_type, new_disease, id): #main loop add 'if no:'
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = "update Patient set name = ?, type = ?, disease = ? where id = ?;"
    values = (new_name, new_type, new_disease, id)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    print("Table has been updated.")

def update_doner(new_name, new_btype, new_number, id): #not finished
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = ''''''
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Table has been sucessfully updated.")

#add
def add_patient(new_name, new_btype, new_disease):
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"insert into patient(name, type, disease) values {new_name}, {new_btype}, {new_disease}"
    cursor.execute(sql)
    db.commit
    db.close()
    print("New patient has been successfully added.")

def delete(table, where, condition): #not finished
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor
    sql = ""
    db.close()


while True:
    print("""\nWelcome to Blood Bank Manage System\n
Tables:
1. Patient
2. Doner
3. Donation
4. Bank  
5. Usage
""")
    table = input("Type number for table you would like to view/alter: ")

    if table == "1": #patient
        fetchall_patient()
        change = input("Type 0 to exit, 1 to update, 2 to add, or 3 to delete a patient: ")
        if change == "0": #exit
            print("Exiting...")
            break
        if change == "1": #update
            id = input("Enter ID: ")
            print("-----\nTo not update a specific field, type 'no'.\n-----")            
            name = input("Enter new name: ")
            if name == "no":
                name = fetch_one("patient", "name", id)
            btype = input("Enter new blood type: ")
            if btype == "no":
                btype = fetch_one("patient", "type", id)
            disease = input("Enter new disease: ")
            if disease == "no":
                disease = fetch_one("patient", "disease", id)
            update_patient(name, btype, disease, id)
            break
        elif change == "2": #add
        elif change == "3": #delete
        else:
            not_valid_num()
            continue
    
    if table == "2": #Doner
        fetchall_doner()
        change = input("Type 0 to exit, 1 to update, 2 to add, or 3 to delete a patient: ")
        if change == "0": #exit
            print("Exiting...")
            break
        # if change == "2":