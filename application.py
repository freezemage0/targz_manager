from entity import *
from tools import *
from event import *

class Application:
    entitiesInitialized = False

    def initialize():
        Application.EntityManager = EntityManager.getInstance()
        Application.SettingsManager = SettingsManager.getInstance()
        entities = Application.EntityManager.getAll()
        for name in entities:
            entityObject = Application.EntityManager.getEntity(name)
            entityObject.initialize()
        Application.entitiesInitialized = True

    def run(main):
        try:
            if Application.entitiesInitialized == False:
                Application.initialize()

            main()

        except Exception as Error:
            exit(Error)
