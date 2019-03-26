from entity import *
from commands import *
from tools import *
from dummy import *

class Application:
    def __init__(self):
        self.EntityManager = EntityManager.getInstance()
        self.CommandManager = CommandManager.getInstance()
        self.entitiesInitialized = False

    def run(self):
        try:
            if self.entitiesInitialized == False:
                entities = self.EntityManager.getAll()
                for name in entities:
                    entityObject = self.EntityManager.getEntity(name)
                    entityObject.initialize()
                self.entitiesInitialized = True

            dummy = self.EntityManager.getEntity('DummyEntity')
            print(dummy.getDummy())
        except Exception as Error:
            exit(Error)

if __name__ == '__main__':
    object = Application()
    object.run()
