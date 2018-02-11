import configparser
import os
from configController import fbPage, twitterStatus

config = configparser.ConfigParser()
configFile = os.path.dirname(os.path.abspath(__file__))+"/source/config.ini"
config.read(configFile)

# facebook test
print('Starting facebook tests')
try:
    post_result = fbPage.post("This is a python test")
    fbPage.delete(post_result['id'])
except:
    print('There is an issue with the Facebook API')

# twitter test
print('Starting twitter tests')
try:
    post_result = twitterStatus.post("This is a python test")
    twitterStatus.delete(post_result.id)
except:
    print('There is an issue with the Twitter API')

# twitter test on threading
print('Starting threading test')
try:
    post_result = twitterStatus.post("This is the first part of the thread")
    reply = twitterStatus.postToThread('This is the second part of the thread', \
            in_reply_to_status_id = post_result.id)
    twitterStatus.delete(post_result.id)
    twitterStatus.delete(reply.id)
except:
    print('There is an issue with the Twitter threading')

print('All tests done!')
