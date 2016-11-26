import configparser
import os
from APIConnectors.fbpageAPI import fbpageAPI

config = configparser.ConfigParser()
configFile = os.path.dirname(os.path.abspath(__file__))+"/source/config.ini"
config.read(configFile)

# test selection
accesstoken = config["facebook"]["accesstoken"]
pageid = config["facebook"]["pageid"]
page = fbpageAPI(accesstoken, pageid)
post_result = page.post("This is a python test")
page.delete(post_result['id'])
