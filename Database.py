import sqlite3
from tabulate import tabulate

def connection():
  try:
    conn = sqlite3.connect('/media/cel00584/My Docs/softwares/consoleApp/sqlite/bin/contactManager.db')
    return conn
  except SQlite3.Error as e:
    return "could not connect to database"



def create_tables():
  conn = connection()
  c = conn.cursor()

  try:
    c.execute('CREATE TABLE IF NOT EXISTS contacts(phoneNumber INTEGER PRIMARY KEY NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(250) NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS messages(messageID INTEGER PRIMARY KEY AUTOINCREMENT, destination INTEGER NOT NULL, content varchar(300) NOT NULL, date_sent timestamp,FOREIGN KEY(destination) REFERENCES contacts(phoneNumber))')
  except sqlite3.Error,e:

    return "Error: %s" %e.args[0]

  conn.commit()
  conn.close()


#Inserts to db new contact details
def insert_to_table(valuelist):

  conn = connection()
  c = conn.cursor()
  try:
    valuelist = tuple(valuelist)
    c.execute('INSERT INTO contacts (first_name,last_name,phoneNumber) values(?,?,?)', valuelist)
    conn.commit()
    return True
  except Exception as e:
    return False
    conn.close()


#def updateTable(newNumber,fname):

  #conn = connection()
  #c = conn.cursor()

  #contactToEdit = fetchData(fname)

  #if contactToEdit != "":
    #c.execute('UPDATE contacts SET phoneNumber = ? WHERE last_name = ?',(newNumber,fname,))
#finish this update query
  #conn.commit()
  #conn.close()

#deletes from db as per user's request
def delete_from_table(fname):

  conn = connection()
  c = conn.cursor()
  try:
    contactToDelete = fetch_data(fname)

    if(contactToDelete is "No data found"):

      return "That contact does not exists."
    else:

      print("1 to confirm you want to delete %s or 2 to ignore request" %contactToDelete)
      confirm = input()

      if confirm == 1:

        c.execute('DELETE FROM contacts WHERE phoneNumber = ?', (contactToDelete,))
        conn.commit()
        return "Contact %d deleted" %contactToDelete

      else: 

        return "Request Ignored"
  except Exception as e: 
    conn.close()



#Retrieves all contact details and display in  atable
def fetch_all_data():
  conn = connection()
  c = conn.cursor()
  main_row_list = []

  try:
    c.execute('SELECT * from contacts')
    no_of_rows = c.fetchall()

    for row in no_of_rows:
      row_list = list(row)
      main_row_list.append(row_list)
      
    #print(main_row_list)  
    table_contacts = main_row_list

    return tabulate(table_contacts)
    conn.commit()
  except Exception as e:
    return "You Have no contacts to view. Kindly add some"
    conn.close()


#fetches data from db and returns the  phone number for specified
def fetch_data(fname):

  name1 = []

  conn = connection()
  c = conn.cursor()
  try:
    c.execute('SELECT count(*) from contacts WHERE first_name = ?',(fname,))

    no_rows = c.fetchall()
    no_rows1 = [int(i[0]) for i in no_rows]


    if no_rows1 == [0]:
      return "No data found"

    else:
      if no_rows1[0] == 1:

        c.execute('SELECT phoneNumber from contacts WHERE first_name = ?',(fname,))
        result = c.fetchall()

        for res_row in result:

          return res_row[0]

      elif no_rows1[0] > 1:

        print("Which %s? (Enter number in [] to select)" %fname)

        c.execute('SELECT last_name from contacts WHERE first_name = ?',(fname,))
        result = c.fetchall()

        for res_row1 in result:

          name1.append(res_row1[0])

        for i in range(0,len(name1)):

          print("[%d] %s" %(i, name1[i]))

        contact = int(input())

        c.execute('SELECT phoneNumber FROM contacts WHERE last_name = ?', (name1[contact],))

        nofrows = c.fetchall()

        for rows in nofrows:

          return rows[0]
    conn.commit()
  except Exception as e:
    return "Sorry. Wrong input"

    conn.close()


#selcts last name like one in input and if exists alets user
def fetch_last_name(lname):

  conn = connection()
  c = conn.cursor()
  try:
    c.execute('SELECT * from contacts WHERE last_name = ?',(lname,))
    no_rows = c.fetchall()
    if no_rows == []:
      return True
    else:
      return False
    conn.commit()
  except Exception as e:
    conn.close()


#sends sms to db
def save_sms(valuelist):

  conn = connection()
  c = conn.cursor()

  valuelist = tuple(valuelist)

  c.execute('INSERT INTO messages (destination,content,date_sent) values(?,?,?)', valuelist)

  conn.commit()
  conn.close()

#Views all sms sent in tabular format
def view_sms():
  conn = connection()
  c = conn.cursor()
  main_row_list = []

  try:
    c.execute('SELECT * from messages')
    no_of_rows = c.fetchall()

    for row in no_of_rows:
      row_list = list(row)
      main_row_list.append(row_list)
      
    #print(main_row_list)  
    table_contacts = main_row_list

    return tabulate(table_contacts)
    conn.commit()
  except Exception as e:
    return "You Have no messages to view."
    conn.close()

#print(fetch_data("nan"))
#updateTable('0725789856','Eunice')
#insertToTable('contacts', ['Eunice','Waj','0705925435'])
