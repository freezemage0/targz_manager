from event import *
class EventHandler:
	def __init__(self):
		self.EventManager = EventManager.getInstance()
		self.EventManager.registerHandler('onApplicationException', self.register)

	def register(self, event):
		print('OnApplicationException Error Text: {}'.format(event.getEventParams()))
		event.setEventParams('I was handled by Event Handler: {}.{}()'.format(
			self.__class__.__name__, self.register.__name__
		))
		return True
