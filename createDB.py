import sqlite3
from tabulate import tabulate

def connection():

  conn = sqlite3.connect('/media/cel00584/My Docs/softwares/consoleApp/sqlite/bin/contactManager.db')
  return conn

def createtables():
  conn = connection()
  c = conn.cursor()

  try:
    c.execute('CREATE TABLE IF NOT EXISTS contacts(phoneNumber INTEGER PRIMARY KEY NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(250) NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS messages(messageID INTEGER PRIMARY KEY AUTOINCREMENT, destination INTEGER NOT NULL,date_sent timestamp,FOREIGN KEY(destination) REFERENCES contacts(phoneNumber))')
 
  except sqlite3.Error,e:

    print "Error: %s" %e.args[0]

  conn.commit()
  conn.close()


def insertToTable(valuelist):

  conn = connection()
  c = conn.cursor()

  valuelist = tuple(valuelist)

  c.execute('INSERT INTO contacts (first_name,last_name,phoneNumber) values(?,?,?)', valuelist)

  conn.commit()
  conn.close()


def updateTable(fname):

  conn = connection()
  c = conn.cursor()

  contactToEdit = fetchData(fname)

  if contactToEdit != "":
    c.execute('UPDATE contacts SET ')
#finish this update query
  conn.commit()
  conn.close()




def deleteFromTable(fname):

  conn = connection()
  c = conn.cursor()

  contactToDelete = fetchData(fname)

  print("1 to confirm you want to delete %d" %contactToDelete)
  confirm = input()

  if confirm == 1:

    c.execute('DELETE FROM contacts WHERE phoneNumber = ?', (contactToDelete,))

    print("Contact %d deleted" %contactToDelete)

  else: 
    print("Request Ignored")

  conn.commit()
  conn.close()




def fetchAllData():
  conn = connection()
  c = conn.cursor()

  main_row_list = []
  c.execute('SELECT * from contacts')
  no_of_rows = c.fetchall()

  for row in no_of_rows:
    row_list = list(row)
    main_row_list.append(row_list)
    
  #print(main_row_list)  
  table_contacts = main_row_list

  return tabulate(table_contacts)

  conn.commit()
  conn.close()



def fetchData(fname):

  name1 = []

  conn = connection()
  c = conn.cursor()

  c.execute('SELECT * from contacts WHERE first_name = ?',(fname,))

  no_rows = c.fetchall()

  if no_rows == 1:

    for row in no_rows:

      return row[0]

  elif no_rows > 1:

    print("Which %s?" %fname)

    for row in no_rows:

      name1.append(row[2])

    for i in range(1,len(name1)):

       print("[%d] %s" %(i, name1[i]))

    contact = int(input())

    c.execute('SELECT phoneNumber FROM contacts WHERE last_name = ?', (name1[contact-1],))

    nofrows = c.fetchall()

    for rows in nofrows:

      return rows[0]


  else:
    
    return "empty set"

  conn.commit()
  conn.close()


#createtables()
#insertToTable('contacts', ['Eunice','Waj','0705925435'])
#fetchAllData()