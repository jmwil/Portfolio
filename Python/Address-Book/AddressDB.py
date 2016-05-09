import sqlite3

conn = sqlite3.connect('AddressBookDB.db')
c = conn.cursor()

jimmy = (1, 'Jimmy Wilcox', 5031234567, 'myemailaddress@gmail.com', '9084 NotMyAddress', '', 'Portland', 'OR', 97225, 'Mars')

contactList = []

namereal = ''
phone = ''
email = ''
addressone = ''
addresstwo = ''
city = ''
state = ''
zipcode = ''
country = ''


def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS addressbook (\
        id INTEGER PRIMARY KEY, \
        name VARCHAR, \
        phone INT(10), \
        email VARCHAR, \
        addressone VARCHAR, \
        addresstwo VARCHAR, \
        city VARCHAR, \
        state VARCHAR, \
        zipcode INT(5), \
        country VARCHAR)")
    c.execute("INSERT OR IGNORE INTO addressbook VALUES (?,?,?,?,?,?,?,?,?,?)", jimmy)
    conn.commit()

def saveContact(name, phone, email, address1, address2, city, state, zipcode, country):
    c.execute("INSERT INTO addressbook (name, phone, email, addressone, addresstwo, city, state, zipcode, country) VALUES (?,?,?,?,?,?,?,?,?)",(name, phone, email, address1, address2, city, state, zipcode, country))
    conn.commit()

def deleteContact(name):
    c.execute("DELETE FROM addressbook WHERE name = ?", [name])
    conn.commit()

def updateContactList():
    global contactList
    c.execute("SELECT name FROM addressbook")
    d = c.fetchall()
    for row in d:
        contactList.append(str(row).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',',''))
    return contactList

def readPhone(name):
    c.execute("SELECT phone FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readEmail(name):
    c.execute("SELECT email FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readAddressOne(name):
    c.execute("SELECT addressone FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readAddressTwo(name):
    c.execute("SELECT addresstwo FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readCity(name):
    ("SELECT city FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readState(name):
    c.execute("SELECT state FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readZipCode(name):
    c.execute("SELECT zipcode FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')

def readCountry(name):
    c.execute("SELECT country FROM addressbook WHERE name = ?", [name])
    p = c.fetchall()
    return str(p).replace(',)','').replace('(','').replace(')','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',','')
