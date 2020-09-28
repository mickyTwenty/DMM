import configparser
import os
import enum
from datetime import datetime

config_file = 'config.ini'
smtp_config_file = 'smtp.ini'

default_rwt = 10

class APP_STATE(enum.Enum):
    NONE                    = -1
    STATE_NEED_LOGIN        = 0
    STATE_NEED_TRUCKID      = 1
    STATE_BEGIN_LIFT        = 2
    STATE_SCAN_BARCODE      = 3

global _App

class AppSettings:
    def __init__(self):
        self.TRUCK_ID = ''
        self.WEIGHTTHRESHOLD = 0
        self.SERIALMODE = ''
        self.WEIGHTMODE = ''
        self.WEIGHTCODE = ''

        self.SMTP_SERVER = None
        self.SMTP_PORT = None
        self.SMTP_EMAIL = None
        self.SMTP_PWD = None
        self.SMTP_CCEMAIL = None

        self.CLIENT_HOST = ''
        self.SAVED_USER = ''

        '''
        self.NETWORK_TYPE = 0
        self.NETWORK_IPADDR = ''
        self.NETWORK_SUBNETMASK = ''
        self.NETWORK_GATEWAY = ''
        self.NETWORK_DNS1 = ''
        self.NETWORK_DNS2 = ''
        '''

        self.load()
        self.loadSMTPConfig()
    
    def load(self):
        print('loading config.ini...')
        config = configparser.ConfigParser()

        config.read(config_file)

        self.TRUCK_ID = config['Settings']['TRUCKID']
        self.WEIGHTTHRESHOLD = config['Settings'].getint('WEIGHTTHRESHOLD')
        self.SERIALMODE = config['Settings']['SERIALMODE']
        self.WEIGHTMODE = config['Settings']['WEIGHTMODE']
        self.WEIGHTCODE = config['Settings']['WEIGHTCODE']

        self.CLIENT_HOST = config['Settings']['CLIENT_HOST']
        self.SAVED_USER = config['Settings']['SAVED_USER']

        '''
        self.NETWORK_TYPE = config['Network'].getint('TYPE')
        self.NETWORK_IPADDR = config['Network']['IPADDR']
        self.NETWORK_SUBNETMASK = config['Network']['SUBNETMASK']
        self.NETWORK_GATEWAY = config['Network']['GATEWAY']
        self.NETWORK_DNS1 = config['Network']['DNS1']
        self.NETWORK_DNS2 = config['Network']['DNS2']
        '''
        if self.WEIGHTTHRESHOLD is None:
            self.WEIGHTTHRESHOLD = default_rwt

    def save(self):
        print('saving config.ini...')
        config = configparser.RawConfigParser()
        config.add_section('Settings')
        config.set('Settings', 'TRUCKID', self.TRUCK_ID)
        config.set('Settings', 'WEIGHTTHRESHOLD', self.WEIGHTTHRESHOLD)
        config.set('Settings', 'SERIALMODE', self.SERIALMODE)
        config.set('Settings', 'WEIGHTMODE', self.WEIGHTMODE)
        config.set('Settings', 'WEIGHTCODE', self.WEIGHTCODE)

        config.set('Settings', 'CLIENT_HOST', self.CLIENT_HOST)
        config.set('Settings', 'SAVED_USER', self.SAVED_USER)

        '''
        config.add_section('Network')
        config.set('Network', 'TYPE', self.NETWORK_TYPE)
        config.set('Network', 'IPADDR', self.NETWORK_IPADDR)
        config.set('Network', 'SUBNETMASK', self.NETWORK_SUBNETMASK)
        config.set('Network', 'GATEWAY', self.NETWORK_GATEWAY)
        config.set('Network', 'DNS1', self.NETWORK_DNS1)
        config.set('Network', 'DNS2', self.NETWORK_DNS2)
        '''

        with open(config_file, 'w') as configfile:
            config.write(configfile)

    def loadSMTPConfig(self):
        print('loading smtp config...')
        config = configparser.ConfigParser()
        config.read(smtp_config_file)
        
        self.SMTP_SERVER = config['SMTP']['SERVER']
        self.SMTP_PORT = config['SMTP'].getint('PORT')
        self.SMTP_EMAIL = config['SMTP']['EMAIL']
        self.SMTP_PWD = config['SMTP']['PASSWORD']
        self.SMTP_CCEMAIL = config['SMTP']['CC']

    def saveSMTPConfig(self):
        print('saving smtp config...')
        config = configparser.RawConfigParser()
        config.add_section('SMTP')
        config.set('SMTP', 'SERVER', self.SMTP_SERVER)
        config.set('SMTP', 'PORT', self.SMTP_PORT)
        config.set('SMTP', 'EMAIL', self.SMTP_EMAIL)
        config.set('SMTP', 'PASSWORD', self.SMTP_PWD)
        config.set('SMTP', 'CC', self.SMTP_CCEMAIL)

        with open(smtp_config_file, 'w') as configfile:
            config.write(configfile)
    
    def getSMTPConfig(self):
        return [self.SMTP_SERVER, self.SMTP_PORT, self.SMTP_EMAIL, self.SMTP_PWD, self.SMTP_CCEMAIL]

class App:
    def __init__(self):
        self.APPSTATE = APP_STATE.NONE

        self.LoginState = False
        self.LoginID = ''

        self.CHECKERSTAT = True
        self.APICALLSTAT = True
        self.TIMESTAT = True
        self.HX711STAT = True
        self.RS232STAT = True
        self.BCSCANSTAT = True
        self.WIFISTAT = True
        self.WIFICONNECTING = False

        self.WIFI_CONNECTION = False
        self.WIFI_SSID = ''
        self.WIFI_PWD = ''

        self.APP_PATH = os.getcwd()

        self.DEBUG = False
        self.KEYBOARD_TEXT = ['']

        self.MESSAGE_ON = False
        self.MESSAGE_TYPE = ''
        self.MESSAGE_TEXT = ''
        self.MESSAGE_DURATION = 0

        self._Settings = AppSettings()

        #self.LoginID = self._Settings.SAVED_USER

    def getDateTimeStamp(self, format):
        now = datetime.now()
        date_time = now.strftime(format)
        return date_time

_App = App()
