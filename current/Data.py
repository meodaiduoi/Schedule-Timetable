import pandas as pd

from ClassScheduleDT import *

'''
DataPhaser:
'''
class DataPhaser:
    
    def __init__(self, room_csv_path: str, meeting_time_csv_path: str, instructor_csv_path: str):
        self._room_df = pd.read_csv(room_csv_path)
        self._mtt_df = pd.read_csv(meeting_time_csv_path)
        self._inst_df = pd.read_csv(instructor_csv_path)

        self._rooms = []; self._meetingTimes = []; self._instructors = []
        self.initilizer()

    def initilizer(self):
        number_room = self._room_df.shape[0]
        number_mtt = self._mtt_df.shape[0]
        number_inst = self._inst_df.shape[0]
        for i in range(0, number_room):
            self._rooms.append(Room(self._room_df.iloc[i]['id'], self._room_df.iloc[i]['seat_capacity']))
        for i in range(0, number_mtt):
            self._meetingTimes.append(Room(self._room_df.iloc[i]['id'], self._room_df.iloc[i]['professor']))
        for i in range(0, number_inst):
            self._instructors.append(Room(self._room_df.iloc[i]['id'], self._room_df.iloc[i]['professor']))

    def getRoom(self):
        return self._rooms;

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

# testRomm = DataPhaser("./data/Room.csv")
# test = Data(testRomm)
# print(test.getRoom()[0].getCapacity())
