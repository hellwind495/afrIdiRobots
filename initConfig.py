import configparser

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

with open('source/config.ini','w') as configFile:
    config.write(configFile)
