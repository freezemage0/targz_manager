from tools import *

@Singleton
class EventManager:
	def __init__(self):
		self.__settings = SettingsManager.getInstance()
		self.__registry = {}

	def getEvents(self):
		return list(self.__registry.keys())

	def registerHandler(self, eventName, handler):
		events = self.getEvents()
		if eventName not in events:
			raise AttributeError(
				'Registry Conflict: Event "{}" does not exist'.format(eventName)
			)
		self.__registry[eventName].append(handler)

	def getHandlers(self, eventName):
		return self.__registry[eventName]

	def executeHandler(self, handler, event):
		executionStatus = handler(event)
		if executionStatus is not False:
			executionStatus = True
		return executionStatus

	def receive(self, event):
		eventName = event.getEventName()
		handlers = self.getHandlers(eventName)
		for handler in handlers:
			if self.executeHandler(handler, event) is False:
				#@TODO: implement EventHandlerException
				raise Exception(
					'Event Handler Error in handler "{}", event "{}"'.format(
						handler.__name__, event.getEventName()
					)
				)
	def registerEvent(self, eventName):
		if eventName not in self.getEvents():
			self.__registry[eventName] = []

class Event:
	def __init__(self, params):
		self.eventName = params['eventName']
		self.eventParams = params['eventParams']

	def send(self):
		eventManager = EventManager.getInstance()
		eventManager.receive(self)

	def getEventName(self):
		return self.eventName

	def getEventParams(self):
		return self.eventParams

	def setEventParams(self, eventParams):
		self.eventParams = eventParams
