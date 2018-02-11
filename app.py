from getIdiom import getIdiom
from sendEmail import sendEmail
from configController import fbPage, twitterStatus
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
    post_result = twitterStatus.post(subject)
    # sendEmail(subject, body)

    # send the second email
    subject = "2/2 Betekenis: %s #Afrikaans" % meaning
    twitterStatus.postToThread(subject, in_reply_to_status_id = post_result.id)
    # sendEmail(subject, body)

    # add a facebook post
    message = "%s\nBetekenis: %s" % (idiom, meaning)
    post_result = fbPage.post(message=message)

# start the application
oneRun()
