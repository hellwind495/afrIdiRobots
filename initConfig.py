import configparser
import os

config = configparser.ConfigParser()
config['Email'] = {}
config['Email']['From'] = 'email@domain.com'
config['Email']['To'] = 'email@domain.com'
config['Email']['host'] = 'smtp.example.com'
config['Email']['port'] = '465'

config['keyring'] = {}
config['keyring']['service'] = ''
config['keyring']['username'] = ''
config['keyring']['password'] = ''

config['facebook'] = {}
config['facebook']['accesstoken'] = ''
config['facebook']['pageid'] = ''
config['facebook']['client_id'] = ''
config['facebook']['client_secret'] = ''

config['twitter'] = {}
config['twitter']['custKey'] = ''
config['twitter']['custSecret'] = ''
config['twitter']['accessToken'] = ''
config['twitter']['accessSecret'] = ''

with open(os.path.dirname(os.path.abspath(__file__))+'/source/config.ini','w') as configFile:
    config.write(configFile)
