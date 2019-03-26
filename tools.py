import time, datetime, configparser
def Singleton(classInstance):
    class Wrapper:
        instance = None
        def __init__():
            raise NotImplementedError()

        def getInstance():
            if Wrapper.instance == None:
                Wrapper.instance = classInstance()
            return Wrapper.instance

    return Wrapper

@Singleton
class SettingsManager:
    def __init__(self):
        self.logLevels = [
            'DEBUG',
            'INFO',
            'WARNING',
            'ERROR',
            'FATAL ERROR'
        ]
        self.configFile = 'config.ini'
        self.config = None
        self.logFile = None
        self.isInitialized = False

    def initialize(self):
        if self.isInitialized == False:
            try:
                self.logLevel = self.getConfigParam('log_level')
                self.logFileName = self.getConfigParam('log_name')
                self.logMask = '<{}> [{}] {}: {}\n'
                self.isInitialized = True
            except Exception as Error:
                Error
        return self.isInitialized

    def log(self, logLevel, logMessage, logInstance):
        self.initialize()
        if logLevel >= int(self.logLevel):
            fullDate = datetime.datetime.now()
            date = '{}:{}:{}'.format(fullDate.hour, fullDate.minute, fullDate.second)
            logLevelName = self.logLevels[logLevel]
            self.getLogger().write(self.logMask.format(
                date, logInstance, logLevelName, logMessage
            ))

    def getConfig(self):
        if self.config == None:
            config = configparser.ConfigParser()
            config.read(self.configFile)
            self.config = config
        return self.config

    def getConfigParam(self, paramName):
        config = self.getConfig()
        if paramName not in config['DEFAULT']:
            raise AttributeError(
                'Parameter "{}" not found in config file'.format(paramName)
            )
        return config['DEFAULT'][paramName]

    def getLogger(self):
        if self.logFile == None:
            filename = self.logFileName + str(int(time.time())) + '.log'
            self.logFile = open(filename, 'w')
        return self.logFile
