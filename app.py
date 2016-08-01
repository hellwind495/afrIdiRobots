from getIdiom import getIdiom
from sendEmail import sendEmail
from datetime import datetime
from datetime import timedelta

import logging
import os

def oneRun():

    logging.basicConfig(filename=os.path.dirname(os.path.abspath(__file__))+"/source/afrIdiRobots.log",level=logging.DEBUG)
    logging.info("START: %s" % datetime.now())

    # get the message you want to send
    ID, idiom, meaning = getIdiom()
    logging.info("EMAIL: Sending ID %s at %s" % (ID, datetime.now()))

    # send the first email
    subject = "1/2 %s #Afrikaans" % idiom
    body = ""
    sendEmail(subject, body)

    # send the second email
    subject = "2/2 Betekenis: %s #Afrikaans" % meaning
    sendEmail(subject, body)

# start the application
oneRun()
