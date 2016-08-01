# Import smtplib for the actual sending function
import smtplib
import configparser
import os

# Import the email modules we'll need
from email.mime.text import MIMEText

def sendEmail(subject, body):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    # with open(textfile) as fp:
        # Create a text/plain message
    config = configparser.ConfigParser()
    configFile = os.path.dirname(os.path.abspath(__file__))+"/source/config.ini"
    config.read(configFile)
    service = config["keyring"]["service"]
    username = config["keyring"]["username"]
    password = config["keyring"]["password"]
    host = config["Email"]["host"]
    port = config["Email"]["port"]
    msg = MIMEText(body)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = subject
    msg['From'] = config['Email']['From']
    msg['To'] = config['Email']['To']

    # Send the message via our own SMTP server.
    server_ssl = smtplib.SMTP_SSL(host, port)
    server_ssl.ehlo()
    server_ssl.login(username, password)
    # password
    server_ssl.send_message(msg)
    server_ssl.quit()
