import configparser
import os
from configController import fbPage, twitterStatus

config = configparser.ConfigParser()
configFile = os.path.dirname(os.path.abspath(__file__))+"/source/config.ini"
config.read(configFile)

# facebook test
print('Starting facebook tests')
post_result = fbPage.post("This is a python test")
fbPage.delete(post_result['id'])

# twitter test
print('Starting twitter tests')
post_result = twitterStatus.post("This is a python test")
twitterStatus.delete(post_result.id)

print('All tests done!')
