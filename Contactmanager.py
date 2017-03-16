import Database 
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

#This function add new contacts  by calling method insertToTable

def add_contact(fname ,lname, pnumber):
	
	Database.create_tables()

	if fname != "" and lname != "":

		if pnumber.isdigit():

			if len(pnumber) == 10:

				pnumber = int('254'+ pnumber[1:10])


				if Database.fetch_last_name(lname) is True:

						Database.insert_to_table([fname,lname,pnumber])

				else:
					return "Sorry! That last name already exixts"

			else:

				return "Phone number inputs more that 10"
		else:

			return "Sorry! Number should be only digits"

	return "Sorry! Names should  not be empty"


#This function search for  exixting contacts  by calling method fetchData with the first name of the contact

def search_contact(fname):

	if fname != "":

		return Database.fetch_data(fname)

	else:

		return "Name should not be empty"



#This function sends text  by calling method fetchData

def send_text(fname,mess):
	listtext = []

	if fname != "":

		to = str(Database.fetch_data(fname))
		to = '+'+ to[0:12]
		print(to)
		message = str(mess)

		username = "eunic"
		apikey   = "dfc6448020ba28879c4f39b39bbc26c80ab1ed3e1ec6cd375d1ff018b1b9350d"

		gateway = AfricasTalkingGateway(username, apikey)
		print(to,message)

		try:

			results = gateway.sendMessage(to, message)
			print(results)

			for recipient in results:


				return 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],recipient['status'],recipient['messageId'],recipient['cost'])

		except AfricasTalkingGatewayException, e:

			return 'Encountered an error while sending: %s' % str(e)
	
	else:

		print("Name should not be empty")


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

	if fname != "":

		return Database.delete_from_table(fname)

	else:

		return "Name should not be empty"




#def syncContatcs():




		

#print(add("Eunice","Wanjiru","0705925432"))


		


