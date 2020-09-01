import configparser

config_file = 'config.ini'

global _App

class AppSettings:
    def __init__(self):
        self.load()
    
    def load(self):
        print('loading config.ini...')
        config = configparser.ConfigParser()
        config.read(config_file)

        self.WEIGHTTHRESHOLD = config['Settings'].getint('WEIGHTTHRESHOLD')
        self.SERIALMODE = config['Settings']['SERIALMODE']
        self.WEIGHTMODE = config['Settings']['WEIGHTMODE']
        self.WEIGHTCODE = config['Settings']['WEIGHTCODE']

    def save(self):
        print('saving config.ini...')
        config = configparser.RawConfigParser()
        config.add_section('Settings')
        config.set('Settings', 'WEIGHTTHRESHOLD', self.WEIGHTTHRESHOLD)
        config.set('Settings', 'SERIALMODE', self.SERIALMODE)
        config.set('Settings', 'WEIGHTMODE', self.WEIGHTMODE)
        config.set('Settings', 'WEIGHTCODE', self.WEIGHTCODE)

        with open(config_file, 'w') as configfile:
            config.write(configfile)



class App:
    def __init__(self):
        self.LoginID = ''

        self.TIMESTAT = True
        self.HX711STAT = True
        self.RS232STAT = True
        self.WIFISTAT = True

        self.WIFI_CONNECTION = False
        self.WIFI_SSID = ''
        self.WIFI_PWD = ''

        self.DEBUG = False
        self.KEYBOARD_TEXT = ['']

        self._Settings = AppSettings()

_App = App()
