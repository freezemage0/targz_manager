from entity import *
from tools import *
from event import *

class Application:
	initialized = False

	def initializeEvents():
		Application.EventManager.registerEvent('onApplicationException')
	
	def initializeEntities():
		entities = Application.EntityManager.getAll()
		for name in entities:
			entityObject = Application.EntityManager.getEntity(name)
			entityObject.initialize()

	def initialize():
		if Application.initialized == False:
			Application.SettingsManager = SettingsManager.getInstance()

			Application.EventManager = EventManager.getInstance()
			Application.initializeEvents()

			Application.EntityManager = EntityManager.getInstance()
			Application.initializeEntities()

			Application.initialized = True

	def run(main):
		try:
			Application.initialize()
			main()
		except AttributeError as ExceptionObject:
			event = Event({
				'eventName': 'onApplicationException',
				'eventParams': ExceptionObject
			})
			event.send()
			ExceptionObject = event.getEventParams()
			exit(ExceptionObject)

