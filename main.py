from application import *
import tar, commands

@Application.run
def main():
	"""
	Getting required entities
	"""
	command = Application.EntityManager.getEntity('CommandEntity')
	tar = Application.EntityManager.getEntity('TarEntity')
	
	commandInfo = command.getArguments()
	Application.SettingsManager.setVerbose(commandInfo['verbose'])
	if commandInfo['help'] == True:
		exit()
	"""
	Preparing settings for TarEntity
	"""
	tarSettings = {
		'project_name': commandInfo['project'],
		'project_folder': Application.SettingsManager.getConfigParam('project_folder'),
		'module_name': commandInfo['module'],
		'module_folder': Application.SettingsManager.getConfigParam('module_folder')
	}
	tar.setSettings(tarSettings)
	tar.execute()
