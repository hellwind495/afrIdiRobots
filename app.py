from getIdiom import getIdiom
from sendEmail import sendEmail
from datetime import datetime
from datetime import timedelta

import getpass
import threading
import logging

logging.basicConfig(filename="source/afrIdiRobots.log",level=logging.DEBUG)
logging.info("START: %s" % datetime.now())

def restart():
    # wait to start again
    now = datetime.now()
    runat = now + timedelta(hours=3)
    delay = (runat - now).total_seconds()

    threading.Timer(delay, oneRun).start()

def oneRun():
    # get the message you want to send
    ID, idiom, meaning = getIdiom()
    logging.info("EMAIL: Sending ID %s at %s" % (ID, datetime.now()))

    # send the first email
    subject = "1/2 %s #Afrikaans" % idiom
    body = ""
    password = getpass.getpass("Enter the password associated with email configured: ")
    sendEmail(password, subject, body)

    # send the second email
    subject = "2/2 Betekenis: %s #Afrikaans" % meaning
    sendEmail(password, subject, body)

    restart()

# start the application
oneRun()
