import pandas as pd

from current.ClassScheduleDT import Department

'''
DataPhaser:
'''
class DataPhaser:
    def __init__(self, room_csv, meeting_time_csv, intructor_csv):
        pass

'''
Data:

'''
class Data:
    def __init__(self, data):
        self._room = data.room
        self._meeting_time = data.meeting_time
        self._instructor = data.instructor
        self._course = data.course
        self._derparment = data.deparment
        self._number_of_class = data._number_of_class

    def getRoom(self): return self._room
    def getMeetingTime(self): return self._meeting_time
    def getInstructor(self): return self._instructor
    def getCourse(self): return self._course
    def getDeparment(self): return self._department
    def getNumberOfClass(self): return self._number_of_class

