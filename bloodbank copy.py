import sqlite3

def fetchall_donation() :
    db = sqlite3.connect('bloodbank_db')
    cursor = db.cursor()
    sql = 'select * from donation;'
    cursor.execute(sql)
    results = cursor.fetchall()

    print("ID  | donerID | doner name          | date      | bankID")
    for donation in results:
        print(f"{donation[0]:<4}| {donation[1]:<8}| {donation[2]:<20}| {donation[3]:<9}| {donation[4]}")
    db.close

if __name__ == "__main__":
    fetchall_donation()



# update donation
# set bankID = 1
# where donation.donerid = (select id from Doner
# where doner.type = 'A+' or doner.type = 'A-');