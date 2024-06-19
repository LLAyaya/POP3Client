from actions.list import list
from actions.top import top
from actions.quit import quit
from actions.dele import delete
from actions.stat import stat
from actions.retr_full import retrieve_full_message
from actions.retr_text import retrieve_text
from actions.NOOP import noop
from actions.rset import rset

import poplib
from email.parser import Parser

# Configuration for the email account
POP3_SERVER = 'pop.gmail.com'
POP3_PORT = 995
EMAIL = 'gtvktn2@gmail.com'
PASSWORD = 'zetj vrfx ewuu hkll'

if __name__ == "__main__":
    # fetch_emails()

    server = poplib.POP3_SSL(POP3_SERVER, POP3_PORT)
    
    server.user(EMAIL)
    server.pass_(PASSWORD)

    # stat(server)
    
    # list(server)

    # retrieve_full_message(server, 55)

    retrieve_text(server, 55)
    
    # top(server, 46, 2)
    
    # noop(server)

    # delete(server, 55)
    # delete(server, 56)
    # delete(server, 54)
    # delete(server, 53)

    # rset(server)

    # quit(server)
    
    
