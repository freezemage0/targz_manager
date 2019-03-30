from entity import *
from event import *
import sys

class CommandEntity(Entity):
	def initialize(self):
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
		return self.arguments

manager = EntityManager.getInstance()
manager.registerEntity(CommandEntity())

