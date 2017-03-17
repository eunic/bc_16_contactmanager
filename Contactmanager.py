import Database 
import datetime
from termcolor import colored, cprint
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

#This function add new contacts  by calling method insertToTable

def add_contact(fname ,lname, pnumber):
	
	Database.create_tables()

	if pnumber.isdigit() is False:
		return colored("Sorry! Number should contain only digits",'red')
			
	elif len(pnumber) != 10:
		return colored("Phone number inputs more that 10",'red')

	elif Database.fetch_last_name(lname) is False:
		return colored("Sorry! That last name already exixts",'red')
	else:
		pnumber = int('254'+ pnumber[1:10])

		if Database.insert_to_table([fname,lname,pnumber]) is True:
			return colored("Successfully added contact",'green')
		else:
			return colored("That phone number exists",'red')


#This function search for  exixting contacts  by calling method fetchData with the first name of the contact

def search_contact(fname):

	return Database.fetch_data(fname)



#This function sends text  by calling method fetchData

def send_text(fname,mess):
	listtext = []
	now = datetime.datetime.now()

	if fname != "":

		to = str(Database.fetch_data(fname))
		to = '+'+ to[0:12]
		message = str(mess)

		username = "eunic"
		apikey   = "dfc6448020ba28879c4f39b39bbc26c80ab1ed3e1ec6cd375d1ff018b1b9350d"

		gateway = AfricasTalkingGateway(username, apikey)

		try:

			results = gateway.sendMessage(to, message)
			listtext =[to,message,now.strftime("%Y-%m-%d %H:%M")]
			Database.save_sms(listtext)

			for recipient in results:

				return 'number=%s;status=%s;messageId=%s' % (recipient['number'],recipient['status'],recipient['messageId'])
			

		except AfricasTalkingGatewayException, e:

			return 'Encountered an error while sending: %s' % str(e)
	
	else:

		return "Name should not be empty"


#This function edits conatct  by calling method updateTable

#def editContact(fname):

	#if fname != "":

		#phonenumber = updateTable(fname)

	#else:

		#return "Name should not be empty"


#This function enables user to view the conatct list by calling method fetchAllData

def view_contact():

	return Database.fetch_all_data()


#This function enables user to delete a conatct by calling method deleteFromTable

def delete_contact(fname):

	return Database.delete_from_table(fname)


def view_message():
	return Database.view_sms()


#def syncContatcs():

#data = cursor.fetchall() #get the rows from your DB
#variable_name = firebase.FirebaseApplication(' your firebase url')
#result = variable_name.post('/', data)
#print("success message")


		

#print(add("Eunice","Wanjiru","0705925432"))


		


