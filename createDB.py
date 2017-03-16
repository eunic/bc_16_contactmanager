import sqlite3
from tabulate import tabulate

def connection():

  conn = sqlite3.connect('/media/cel00584/My Docs/softwares/consoleApp/sqlite/bin/contactManager.db')
  return conn

def create_tables():
  conn = connection()
  c = conn.cursor()

  try:
    c.execute('CREATE TABLE IF NOT EXISTS contacts(phoneNumber INTEGER PRIMARY KEY NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(250) NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS messages(messageID INTEGER PRIMARY KEY AUTOINCREMENT, destination INTEGER NOT NULL,date_sent timestamp,FOREIGN KEY(destination) REFERENCES contacts(phoneNumber))')
 
  except sqlite3.Error,e:

    print "Error: %s" %e.args[0]

  conn.commit()
  conn.close()


def insert_to_table(valuelist):

  conn = connection()
  c = conn.cursor()

  valuelist = tuple(valuelist)

  c.execute('INSERT INTO contacts (first_name,last_name,phoneNumber) values(?,?,?)', valuelist)

  conn.commit()
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


def delete_from_table(fname):

  conn = connection()
  c = conn.cursor()

  contactToDelete = fetch_data(fname)

  print("1 to confirm you want to delete %d" %contactToDelete)
  confirm = input()

  if confirm == 1:

    c.execute('DELETE FROM contacts WHERE phoneNumber = ?', (contactToDelete,))

    print("Contact %d deleted" %contactToDelete)

  else: 
    print("Request Ignored")

  conn.commit()
  conn.close()




def fetch_all_data():
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



def fetch_data(fname):

  name1 = []

  conn = connection()
  c = conn.cursor()

  c.execute('SELECT count(*) from contacts WHERE first_name = ?',(fname,))

  no_rows = c.fetchall()
  no_rows1 = [int(i[0]) for i in no_rows]

  if(no_rows1 != []):

    if no_rows1[0] == 1:

      c.execute('SELECT phoneNumber from contacts WHERE first_name = ?',(fname,))
      result = c.fetchall()

      for res_row in result:

        return res_row[0]

    elif no_rows1[0] > 1:

      print("Which %s?" %fname)

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

  else:
    
    return "No data found"

  conn.commit()
  conn.close()


def fetch_last_name(lname):

  conn = connection()
  c = conn.cursor()

  c.execute('SELECT * from contacts WHERE last_name = ?',(lname,))

  no_rows = c.fetchall()

  if no_rows == []:

    return True

  else:

    return False

  conn.commit()
  conn.close()

#print(fetch_data("nan"))
#updateTable('0725789856','Eunice')
#insertToTable('contacts', ['Eunice','Waj','0705925435'])
