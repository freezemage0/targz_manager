from tools import *

@Singleton
class EntityManager:
    def __init__(self):
        self.__registry = {}
        self.__settingsManager = SettingsManager.getInstance()
        self.__settingsManager.log(
            0,
            'Initialized EntityManager',
            'Application'
        )

    def registerEntity(self, entity):
        name = entity.getName()
        self.__settingsManager.log(
            0,
            'Started registerEntity method for Entity "{}"'.format(name),
            'EntityManager'
        )
        if name in self.getAll():
            self.__settingsManager.log(
                4,
                'Failed to register Entity: Registry Conflict for Entity "{}"'.format(name),
                'EntityManager'
            )
            raise AttributeError('Registry conflict: {}'.format(name))
        self.__settingsManager.log(
            0,
            'Successfully registered Entity "{}"'.format(name),
            'EntityManager'
        )
        self.__registry[name] = entity

    def getAll(self):
        self.__settingsManager.log(
            0,
            'Fetching list of registered Entities',
            'EntityManager'
        )
        return list(self.__registry.keys())

    def getEntity(self, name):
        self.__settingsManager.log(
            0,
            'Started Fetching Entity by name "{}"'.format(name),
            'EntityManager'
        )
        if name not in self.getAll():
            self.__settingsManager.log(
                4,
                'Failed to Fetch Entity: Entity "{}" not registered'.format(name),
                'EntityManager'
            )
            raise AttributeError('Registry not found: {}'.format(name))
        entity = self.__registry[name]
        self.__settingsManager.log(
            0,
            'Successfully Fetched Entity "{}"'.format(name),
            'EntityManager'
        )
        return entity

class Entity:
    def __init__(self):
        self.settingsManager = SettingsManager.getInstance()

    def getName(self):
        return self.__class__.__name__
