from application import *
import tar, commands

@Application.run
def main():
	"""
	Getting required entities
	"""
	SettingsManager = Application.SettingsManager
	
	if commandInfo['help'] == True:
		exit()
	"""
	Preparing settings for TarEntity
	"""
	tarSettings = {
		'project_name': commandInfo['project'],
		'project_folder': Application.SettingsManager.getConfigParam('project_folder'),
		'module_name': commandInfo['module'],
		'module_folder': Application.SettingsManager.getConfigParam('module_folder'),
		'file_mask': Application.SettingsManager.getConfigParam('file_mask')
	}
	tar.setSettings(tarSettings)
	tar.execute()
