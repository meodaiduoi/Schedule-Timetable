from Data import Data
from Schedule import Schedule
class Population:
    def __init__(self, size, data: Data):
        self._size = size
        self._data = data
        self._schedule = []
        for i in range(0, size):
            self._schedule.append(Schedule().initialize())

    def getSchedule(self): return self._schedule