from tools import Singleton

@Singleton
class CommandManager:
    def __init__(self):
        self.__commands = ['!начать', '!описание', '!очки', '!выйти']

    def processCommand(self, string):
        signal = self.__commands.find(string)
        if signal < 0:
            return False
        self.__lastSignal = signal

    def getSignal(self):
        return self.__lastSignal
