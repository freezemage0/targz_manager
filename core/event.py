from tools import *

@Singleton
class EventManager:
	def __init__(self):
		self.__settings = SettingsManager.getInstance()
		self.__registry = {}

	def getEvents(self):
		self.__settings.logger.log(
			0, 'Getting List of Events', 'EventManager'
		)
		return list(self.__registry.keys())

	def registerHandler(self, eventName, handler):
		events = self.getEvents()
		self.__settings.logger.log(
			0, 'Checking if event handler is registered', 'EventManager'
		)
		if eventName not in events:
			self.__settings.logger.log(
				4, 'Registry Conflict: Event "{}" does not exist'.format(eventName), 'EventManager'
			)
			raise AttributeError(
				'Registry Conflict: Event "{}" does not exist'.format(eventName)
			)
		self.__settings.logger.log(
			0, 'Successfully registered Handler for "{}" Event'.format(eventName), 'EventManager'
		)
		self.__registry[eventName].append(handler)

	def getHandlers(self, eventName):
		self.__settings.logger.log(
			0, 'Getting List of Event Handlers', 'Eventmanager'
		)
		return self.__registry[eventName]

	def executeHandler(self, handler, event):
		executionStatus = handler(event)
		if executionStatus is not False:
			executionStatus = True
		return executionStatus

	def receive(self, event):
		self.__settings.logger.log(
			0, 'Event occurred, checking all registered Handlers', 'EventManager'
		)
		eventName = event.getEventName()
		handlers = self.getHandlers(eventName)
		for handler in handlers:
			self.__settings.logger.log(
				0, 'Calling registered EventHandlers', 'EventManager'
			)
			if self.executeHandler(handler, event) is False:
				handlerErrorMsg = 'Event Handler Error in handler "{}", event "{}"'.format(
					handler.__name__, event.getEventName()
				)
				self.__settings.logger.log(0, handlerErrorMsg, 'EventManager')
				#@TODO: implement EventHandlerException
				raise Exception(handlerErrorMsg)

	def registerEvent(self, eventName):
		self.__settings.logger.log(
			0, 'Registering Event "{}"'.format(eventName), 'EventManager'
		)
		if eventName not in self.getEvents():
			self.__registry[eventName] = []

class Event:
	def __init__(self, params):
		self.__settings = SettingsManager.getInstance()
		self.__settings.logger.log(
			0, 'Initializing Event, parameters: {}'.format(params), 'Event'
		)
		self.eventName = params['eventName']
		self.eventParams = params['eventParams']

	def send(self):
		self.__settings.logger.log(
			0, 'Sent Event "{}" signal'.format(self.getEventName), 'Event'
		)
		eventManager = EventManager.getInstance()
		eventManager.receive(self)

	def getEventName(self):
		return self.eventName

	def getEventParams(self):
		return self.eventParams

	def setEventParams(self, eventParams):
		self.__settings.logger.log(
			0, 'Applying new Event Parameters', 'Event'
		)
		self.eventParams = eventParams
