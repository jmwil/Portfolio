import sqlite3

webTemplates = (
    ('Spring Break','We have new deals for Spring Break - Check back soon for more content!'),
    ('Christmas Blowout', 'It\'s everybody\'s favorite time of year! We\'re celebrating the season with some major discounts on all of our high end goods! Don\'t miss this sale!'),
    ('National Cat Day', 'What better way to celebrate this holiday than a sale on all of our cat merchandise! Your cats will love the selection of catnip we have to offer.'),
    ('Zetus Lapetuz!', 'Zenon Carr, GIRL OF THE 21ST CENTURY will be coming to the store this weekend for a book signing. ZOMG!')
    )


conn = sqlite3.connect('WebPageDB.db')
c = conn.cursor()

temparray = []

def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS templates (webTitle VARCHAR(50) PRIMARY KEY, webContent VARCHAR)")
    c.executemany("INSERT OR IGNORE INTO templates (webTitle, webContent) VALUES (?,?)", webTemplates)

def insert(title, content):
    c.execute("INSERT INTO templates (webTitle, webContent) VALUES (?,?)", (title, content))
    conn.commit()

def loadTemplates(title):
    c.execute("SELECT webContent FROM templates WHERE webTitle = ?", [title])
    d = c.fetchone()
    return str(d)

def read():
    global temparray
    del temparray [:]
    c.execute("SELECT webTitle FROM templates")
    d = c.fetchall()
    for row in d:
        temparray.append(str(row).replace(',)','').replace('(','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',',''))
    print(temparray)
    return temparray


#    for i in d:
#        temparray.append(str(i).replace(',)','').replace('(','').replace('u\'','').replace("'","").replace(']','').replace('[','').replace(',',''))
#        return temparray
