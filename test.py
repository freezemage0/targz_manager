from entity import *
from tools import *

class DummyEntity(Entity):
    def __init__(self):
        self.settingsManager = SettingsManager.getInstance()
        self.settingsManager.log(
            0,
            'Using internal constructor to initialize Entity',
            self.getName()
        )
        self.dummyProperty = None

    def initialize(self):
        self.settingsManager.log(
            0,
            'Using initialize() method to initialize Entity Properties',
            self.getName()
        )
        if self.dummyProperty == None:
            self.dummyProperty = True
        self.settingsManager.log(
            0,
            'Successfully Initialized Entity properties',
            self.getName()
        )
    def getDummy(self):
        self.settingsManager.log(
            1,
            'Started getDummy() method',
            self.getName()
        )
        dummy = self.dummyProperty
        self.settingsManager.log(
            1,
            'Successfully fetched dummyProperty',
            self.getName()
        )
        return dummy

mng = EntityManager.getInstance()
mng.registerEntity(DummyEntity())
