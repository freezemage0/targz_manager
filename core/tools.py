import time, datetime, configparser, sys
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

class Logger:
	def __init__(self, logLevel, logFileName, verbose):
		self.logLevels = [
			'DEBUG',
			'INFO',
			'WARNING',
			'ERROR',
			'FATAL ERROR'
		]
		self.logFileName = logFileName
		self.logFile = None
		self.logMask = '<{}> [{}] {}: {}\n'
		self.logLevel = logLevel
		self.verbose = verbose

	def log(self, logLevel, logMessage, logInstance):
		if logLevel >= int(self.logLevel):
			fullDate = datetime.datetime.now()
			date = '{}:{}:{}'.format(fullDate.hour, fullDate.minute, fullDate.second)
			logLevelName = self.logLevels[logLevel]
			preparedMessage = self.logMask.format(date, logInstance, logLevelName, logMessage)
			self.getLoggerFile().write(preparedMessage)
			if self.verbose:
				print(preparedMessage, end='')

	def getLoggerFile(self):
		if self.logFile == None:
			self.logFile = open(self.logFileName, 'w')
		return self.logFile

class ArgvParser:
	class ArgvParserResult:
		def __init__(self, params):
			self.verbose = params['verbose']
			self.help = params['help']
			self.projectName = params['project']
			self.moduleName = params['module']
	
	def __init__(self):
		self.arguments = {
			'help': False,
			'verbose': False,
			'project': '',
			'module': ''
		}
		self.rawArguments = sys.argv
		self.isPrepared = False

	def prepareArguments(self):
		scriptname = self.rawArguments.pop(0)
		self.getSimpleCommands()
		self.getComplexCommands()
		self.isPrepared = True

	def getCommandAliases(self, aliasName):
		aliases = {
            'project': ['-p', '--project'],
            'module': ['-n', '--name'],
            'help': ['-h', '--help', '?'],
            'verbose': ['-v', '--verbose']
        }
		if aliasName not in aliases:
			return []
		return aliases[aliasName]

	def getSimpleCommands(self):
		verbose = self.getCommandAliases('verbose')
		help = self.getCommandAliases('help')
		indexes = []
		for argumentIndex, argumentValue in enumerate(self.rawArguments):
			if argumentValue in verbose:
				self.arguments['verbose'] = True
				indexes.append(argumentIndex)
			if argumentValue in help:
				self.arguments['help'] = True
				indexes.append(argumentIndex)
		indexes.reverse()
		for index in indexes:
			del self.rawArguments[index]

	def getComplexCommands(self):
		project = self.getCommandAliases('project')
		module = self.getCommandAliases('module')
		for argumentIndex, argumentValue in enumerate(self.rawArguments):
			try:
				if argumentValue in project:
					self.arguments['project'] = self.rawArguments[argumentIndex+1]
				if argumentValue in module:
					self.arguments['module'] = self.rawArguments[argumentIndex+1]
			except IndexError:
				continue

	def getArguments(self):
		if self.isPrepared == False:
			self.prepareArguments()
		return self.ArgvParserResult(self.arguments)

@Singleton
class SettingsManager:
	def __init__(self):
		self.configFile = 'config.ini'
		self.config = None
		self.logger = None
		self.parseResult = None
		self.isInitialized = False

	def initialize(self):
		if self.isInitialized == False:
			argvParser = ArgvParser()
			logLevel = self.getConfigParam('log_level')
			logFileName = self.getConfigParam('log_name')

			self.parseResult = argvParser.getArguments()				
			self.logger = Logger(logLevel, logFileName, self.parseResult.verbose)

			self.isInitialized = True
		return self.isInitialized

	def getConfig(self):
		if self.config == None:
			config = configparser.ConfigParser()
			config.read(self.configFile)
			self.config = config['DEFAULT']
		return self.config

	def getConfigParam(self, paramName):
		config = self.getConfig()
		if paramName not in config:
			raise AttributeError(
				'Parameter "{}" not found in config file'.format(paramName)
			)
		return config[paramName]

	def getHelp(self): pass


if __name__ == '__main__':
	sm = SettingsManager.getInstance()
	sm.initialize()
	sm.logger.log(2, sm.parseResult.__dict__, 'SettingsManager')
