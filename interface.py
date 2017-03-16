"""
Note below commands for interacting with app
Usage: 
    my_manager add -n <firstname> <lastname> -p <phone no>
    my_manager search <firstname>
    my_manager text <firstname> <message>...
    my_manager delete <firstname>
    my_manager view 
    my_manager (-h | --help)
    my_manager (-i | --interactive)


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import os
import sys
import sqlite3
import cmd
from docopt import docopt, DocoptExit
#from test import view_contacts
import Contactmanager
from Contactmanager import add_contact,view_contact,delete_contact,search_contact,send_text
from Database import create_tables



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)


    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn



class MycontactManager(cmd.Cmd):

    print("Welcome To Contact Manager")
    prompt = "cmanager->>"
    file = None

    @docopt_cmd
    def do_add(self, args):
        """
        Usage: add -n <firstname> <lastname> -p <phone_no>
        """
        Contactmanager.add_contact(args['<firstname>'],args['<lastname>'],args['<phone_no>'])

    @docopt_cmd
    def do_search(self,args):
        """usage: search <firstname>"""
        print(Contactmanager.search_contact(args['<firstname>']))

    @docopt_cmd
    def do_text(self,args):
        """usage: text <firstname> <message>..."""
        mess = args['<message>']
        mess =" ".join(mess)

        print(Contactmanager.send_text(args['<firstname>'], mess))

    @docopt_cmd
    def do_delete(self,args):
        """usage: delete <firstname>"""
        print(Contactmanager.delete_contact(args['<firstname>']))


    @docopt_cmd
    def do_view(self,args):
        """usage: view"""
        print(Contactmanager.view_contact())

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Thankyou for Using Contact manager!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        MycontactManager().cmdloop()
    except KeyboardInterrupt:
        print('Thankyou for Using Contact manager!')
        exit()
print(opt)