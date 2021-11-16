import pandas as pd

from ClassScheduleDT import *

'''
DataPhaser:
'''
class DataPhaser:
    
    def __init__(self, room_csv_path: str, meeting_time_csv_path: str, instructor_csv_path: str):
        self._room_df = pd.read_csv(room_csv_path)
        self._mtt_df = pd.read_csv(meeting_time_csv_path)
        self._room_df.head(0)

        self._room_
    def initilizer(self):
        for i in _room_df: 
            room: Room = Room(self._room_df., self._room_df['seat_capacity'][i].values())
    
    def getRoom(self):
        return room

    def getMeetingTime(self):
        pass

    def getInstructor(self):
        pass

    def getCourse(self):
        pass

    def getDepartment(self):
        pass

    def getNumberOfClass(self):
        pass


'''
Data:

'''
class Data:
    def __init__(self, data: DataPhaser):
        self._room = data.getRoom()
        self._meeting_time = data.getMeetingTime()
        self._instructor = data.getInstructor()
        self._course = data.getCourse()
        self._derparment = data.getDepartment()
        self._number_of_class = data.getNumberOfClass()

    def getRoom(self): return self._room
    def getMeetingTime(self): return self._meeting_time
    def getInstructor(self): return self._instructor
    def getCourse(self): return self._course
    def getDeparment(self): return self._department
    def getNumberOfClass(self): return self._number_of_class

