import configparser
import os

config = configparser.ConfigParser()
configFile = os.path.dirname(os.path.abspath(__file__))+"/config.ini"
config.read(configFile)
accesstoken = config["facebook"]["accesstoken"]
pageid = config["facebook"]["pageid"]
page = fbpageAPI(accesstoken, pageid)
page.post("This is a python test")
