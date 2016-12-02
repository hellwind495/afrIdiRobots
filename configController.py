import configparser
import os
from APIConnectors.fbpageAPI import fbpageAPI
from APIConnectors.twitterAPI import twitterAPI

config = configparser.ConfigParser()
configFile = os.path.dirname(os.path.abspath(__file__))+"/source/config.ini"
config.read(configFile)

# facebook connection
facebook = config["facebook"]
accesstoken = facebook["accesstoken"]
pageid = facebook["pageid"]
client_id = facebook["client_id"]
client_secret = facebook["client_secret"]
fbPage = fbpageAPI(accesstoken, pageid)
facebook["accesstoken"] = fbPage.generateNewToken(client_id=client_id,client_secret=client_secret)

# twitter connection
twitter = config["twitter"]
custKey = twitter["custKey"]
custSecret = twitter["custSecret"]
accessToken = twitter["accessToken"]
acessSecret = twitter["accessSecret"]
twitterStatus = twitterAPI(custKey,custSecret,accessToken,acessSecret)
