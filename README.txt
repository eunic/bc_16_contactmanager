Hello! Welcome to Contact Manager

With this application you can:

Add contacts
View contacts
Delete contacts
search for a contact
send sms to a contact
view all sms sent out

Requirements:

You will need to install below
docopt==0.6.2
pyfiglet==0.7.5
tabulate==0.7.7
termcolor==1.1.0


Below are the commands to interact with the app.

Note: For now it supports only Kenyan numbers

Usage: 
    my_manager add -n <firstname> <lastname> -p <phone no>
    my_manager search <firstname>
    my_manager text <firstname> <message>...
    my_manager delete <firstname>
    my_manager view
    my_manager viewsms 
    my_manager (-h | --help)
    my_manager (-i | --interactive)


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

