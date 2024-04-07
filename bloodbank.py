import sqlite3

quit = False

def not_valid_num(value):
    print(f"\n'{value}' isn't a valid value. Please type a correct number.")

def exit():
    print("\nExiting...")

def ask_which_function():
    change = input("\nType 0 to return to table menu, 1 to update, 2 to add, or 3 to delete: ")
    return change

def fetch_one(column, table, id): #need to fix
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"select {column} from {table} where id = {id};"
    cursor.execute(sql)
    results = cursor.fetchone()
    db.close()
    return results


#fetchall
def fetchall_patient():
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = ' select * from patient;'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
def printall_patient(results): 
    print("\nPatient:")
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
    print("\nDoner:")
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
    print("\nDonation:")
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
    print("\nBank:")
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
    print("\nUsage:")
    print("ID  | pateintID | donerID | date")
    for usage in results:
        print(f"{usage[0]:<4}| {usage[1]:<10}| {usage[2]:<8}| {usage[3]}")


#update
def update_patient(new_name, new_btype, new_disease, id): #main loop add 'if no:'
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"update Patient set name = '{new_name}', type = '{new_btype}', disease = '{new_disease}' where id = {id};"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Table has been updated.")

def update_doner(new_name, new_btype, new_number, id):
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"update Doner set name = '{new_name}', type = '{new_btype}', number = '{new_number}' where id = {id};"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Table has been sucessfully updated.")

def update_donation(new_donerid, new_dname, new_date, new_bankid, id): #main loop에서 donerid 넣으면 doner name도 fetch하기
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"update Donation set donerID = {new_donerid}, doner_name = '{new_dname}', date = '{new_date}', bankID = {new_bankid} where id = {id};"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Table has been sucessfully updated.") #how to put null values when updating

def update_bank(new_address, id):
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"update Bank set address = '{new_address}' where id = {id};"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Table has been sucessfully updated.")

def update_usage(new_pid, new_did, new_date, id):
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"update Usage set patientID = '{new_pid}', donerID = '{new_did}', date = '{new_date}' where id = {id};"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Table has been sucessfully updated.")


#add
def add_patient(new_name, new_btype, new_disease): #doesn't add
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = f"insert into Patient (name, type, disease) values ('{new_name}', '{new_btype}', '{new_disease}');"
    cursor.execute(sql)
    db.commit
    db.close()
    print("New patient has been successfully added.")

def add_doner(name, btype, number):
    db = sqlite3.connect('bloodbank_db')

def add_donation(donerid, dname, date, bankid):
    db = sqlite3.connect('bloodbank_db')

def add_bank(address):
    db = sqlite3.connect('bloodbank_db')

def add_usage(pid, did, date):
    db = sqlite3.connect('bloodbank_db')


#delete
def delete(table, where, condition): #doesn't delete
    check = input("\nWould you really like to delete this patient?\nType 0 to exit, otherwise type any key to continue: ")
    if check == "0":

        return
    else:
        db = sqlite3.connect('bloodbank_db')
        cursor = db.cursor
        sql = f"delete from {table} where {where} = {condition}"
        print("Patient has been deleted.")
        db.close()
        return


while not quit:
    print("""\nWelcome to Blood Bank Manage System\n
Tables:
1. Patient
2. Doner
3. Donation
4. Bank  
5. Usage
""")
    table = input("Type 0 to exit,\nOtherwise type number for table you would like to view/alter: ")

    if table == "0":
        exit()
        quit = True
        continue
    
    if table == "1": #Patient
        printall_patient(fetchall_patient())
        while True:
            change = ask_which_function()
            if change == "0": #goback
                break
            elif change == "1": #update
                id = input("Enter ID: ")
                print("------------------------------------------\nTo not update a specific field, type 'no'.\n------------------------------------------")            
                name = input("Enter new name: ")
                if name == "no":
                    name = fetch_one("name", "patient", id)
                btype = input("Enter new blood type: ")
                if btype == "no":
                    btype = fetch_one("type", "patient", id)
                disease = input("Enter new disease: ")
                if disease == "no":
                    disease = fetch_one("disease", "patient", id)
                update_patient(name, btype, disease, id)
                continue
            elif change == "2": #add
                name = input("Enter patient's name: ")
                btype = input("Enter patient's blood type: ")
                disease = input("Enter patient's disease: ")
                add_patient(name, btype, disease)
                continue
            elif change == "3": #delete
                table = "patient"
                where = input("Type column name of condition: ") #too complicated for user? fix all below if fix is needed
                condition = input("Type value of condition: ")
                delete(table, where, condition)
                continue
            else:
                not_valid_num(change)
                continue
    
    elif table == "2": #Doner
        printall_doner(fetchall_doner())
        while True:
            change = ask_which_function()
            if change == "0": #goback
                break
            if change == "1": #update
                id = input("Enter ID: ")
                print("------------------------------------------\nTo not update a specific field, type 'no'.\n------------------------------------------")    
                name = input("Enter new name: ")
                if name == "no":
                    name = fetch_one("name", "doner", id)
                btype = input("Enter new blood type: ")
                if btype == "no":
                    btype = fetch_one("type", "doner", id)
                number = input("Enter new phone number: ")
                if number == "no":
                    number = fetch_one("number", "doner", id)
                update_doner(name, btype, number, id)
                continue
            elif change == "2": #add
                name = input("Enter doner's name: ")
                btype = input("Enter doner's blood type: ")
                number = input("Enter doner's number: ")
                add_doner(name, btype, number)
                continue
            elif change == "3": #delete
                table = "doner"
                where = input("Type column name of condition: ") 
                condition = input("Type value of condition: ")
                delete(table, where, condition)
                continue
            else:
                not_valid_num(change)
                continue

    elif table == "3": #Donation
        printall_donation(fetchall_donation())
        while True:
            change = ask_which_function()
            if change == "0": #goback
                break
            elif change == "1": #update
                id = input("Enter ID: ")
                print("------------------------------------------\nTo not update a specific field, type 'no'.\n------------------------------------------")    
                donerid = input("Enter new DonerID: ")
                if donerid == "no":
                    donerid = fetch_one("donerID", "Donation", id)
                dname = input("Enter new doner_name: ")
                if dname == "no":
                    dname = fetch_one("doner_name", "Donation", id)
                date = input("Enter new date: ")
                if date == "no":
                    date = fetch_one("date", "Doantion", id)
                bankid = input("Enter new bankID: " )
                if bankid == "no":
                    bankid = fetch_one("bankID", "Donation", id)
                update_donation(donerid, dname, date, bankid, id)  
                continue
            elif change == "2": #add
                donerid = input("Enter donerID of this donation: ")
                dname = input("Enter doner_name of this donation: ")
                date = input("Enter date of this donation: ")
                bankid = input("Enter bankID of this donation: ")
                add_donation(donerid, dname, date, bankid)
                continue
            elif change == "3": #delete
                table = "donation"
                where = input("Type column name of condition: ") 
                condition = input("Type value of condition: ")
                delete(table, where, condition)
                continue
            else:
                not_valid_num(change)
                continue

    elif table == "4": #Bank
        printall_bank(fetchall_bank())
        while True:
            change = ask_which_function
            if change == "0": #goback
                break
            elif change == "1": #update
                id = input("Enter ID: ")
                print("------------------------------------------\nTo not update a specific field, type 'no'.\n------------------------------------------")    
                address = input("Enter new adress: ")
                if address == "no":
                    address = fetch_one("address", "Bank", id)
                update_bank(address, id)
                continue
            elif change == "2": #add
                address = input("Enter bank's address: ")
                add_bank(address)
                continue
            elif change == "3": #delete
                table = "bank"
                where = input("Type column name of condition: ") 
                condition = input("Type value of condition: ")
                delete(table, where, condition)
                continue
            else:
                not_valid_num(change)
                continue

    elif table == "5": #Usage
        printall_usage(fetchall_usage())
        while True:
            change = ask_which_function()
            if change == "0": #goback
                break
            elif change == "1": #update
                id = input("Enter ID: ")
                print("------------------------------------------\nTo not update a specific field, type 'no'.\n------------------------------------------")    
                pid = input("Enter new Patient ID: ")
                if pid == "no":
                    pid = fetch_one("patientID", "Usage", id)   
                did = input("Enter new Doner ID: ")
                if did == "no":
                    did = fetch_one("donerID", "Usage", id)
                date = input("Enter new date: ")
                if date == "no":
                    date = fetch_one("date", "Usage", id)
                update_usage(pid, did, date, id)
                continue
            elif change == "2": #add
                pid = input("Enter Patient ID of this Usage: ")
                did = input("Enter Doner ID of this Usage: ")
                date = input("Enter date of this Usage: ")
                add_usage(pid, did, date)
                continue
            elif change == "3": #delete
                table = "Usage"
                where = input("Type column name of condition: ") 
                condition = input("Type value of condition: ")
                delete(table, where, condition)
                continue
            else:
                not_valid_num(change)
                continue
    else:
        not_valid_num(table)
        continue