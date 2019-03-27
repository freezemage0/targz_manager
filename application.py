from entity import *
from tools import *
from event import *

class Application:
    initialized = False

    def initialize():
		if Application.initialized == False:
		    Application.EntityManager = EntityManager.getInstance()
		    Application.SettingsManager = SettingsManager.getInstance()
		    entities = Application.EntityManager.getAll()
		    for name in entities:
		        entityObject = Application.EntityManager.getEntity(name)
		        entityObject.initialize()
		    Application.initialized = True

    def run(main):
        try:
			#OnBeforeAppInit
            Application.initialize()
			#OnAfterAppInit
			#OnBeforeMainLogic
            main()
			#OnAfterMainLogic
        except Exception as Error:
			#OnApplicationException
            exit(Error)
