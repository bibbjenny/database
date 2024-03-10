import sqlite3

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

