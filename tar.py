from entity import *
from tools import *
import os, tarfile, time

class TarEntity(Entity):
	def __init__(self):
		self.settingsManager = SettingsManager.getInstance()

	def initialize(self):
		self.projectFolder = None
		self.moduleFolder = None
		self.moduleName = None
		self.projectName = None
		self.path = None
		
	def checkProjectFolder(self):
		projectFolder = self.getPath()
		projectName = self.projectName
		isProjectInFolder = projectName in os.listdir(projectFolder)
		return isProjectInFolder

	def checkModuleFolder(self):
		path = self.getPath() + self.moduleFolder
		isModuleInFolder = self.moduleName in os.listdir(path)
		return isModuleInFolder	
		
	def backup(self):
		os.chdir(self.getPath())
		filename = self.moduleName + '.tar.gz'
		timestamp = str(int(time.time()))
		path = self.getPath()
		if filename in os.listdir():
			newFilename = '{}_backup_{}.tar.gz'.format(
				self.moduleName, timestamp
			)
			os.rename(filename, newFilename)
		self.makeTar(filename)

	def makeTar(self, filename):
		tar = tarfile.TarFile.open(filename, 'w:gz')
		tar.add(self.moduleName, filter = self.tarFilter)
		tar.close()

	def getPath(self):
		if self.path == None:
			self.updatePath()
		return self.path

	def updatePath(self, string=None):
		if string == None:
			path = self.projectFolder.strip('/')
			self.path = '/{}/'.format(path)
		else:
			string = string.strip('/')
			path = self.path.strip('/')
			self.path = '/{}/{}/'.format(path, string)
	
	def setSettings(self, settings):
		try:
			self.projectFolder = settings['project_folder']
			self.moduleFolder = settings['module_folder']
			self.projectName = settings['project_name']
			self.moduleName = settings['module_name']
			self.fileMask = settings['file_mask'].split(',')
		except KeyError as key:
			raise Exception('Missing required parameter: {}'.format(key))

	def execute(self):
		isProjectInFolder = self.checkProjectFolder()
		if isProjectInFolder == False:
			return False
		self.updatePath(self.projectName)
		isModuleInFolder = self.checkModuleFolder()
		if isModuleInFolder == False:
			return False
		self.updatePath(self.moduleFolder)
		self.backup()
		return True

	def tarFilter(self, info):
		mask = self.fileMask
		mask.append('backup')
		for f in mask:
			if f in info.name:
				return None
		return info

manager = EntityManager.getInstance()
manager.registerEntity(TarEntity())
