import pandas as pd

from ClassScheduleDT import *
class Data:
    
    def __init__(self, room_csv_path: str, meeting_time_csv_path: str, instructor_csv_path: str, department_csv_path: str, course_csv_path: str):
        self._room_df = pd.read_csv(room_csv_path)
        self._mtt_df = pd.read_csv(meeting_time_csv_path)
        self._dept_df = pd.read_csv(department_csv_path)
        self._inst_df = pd.read_csv(instructor_csv_path)
        self._course_df = pd.read_csv(course_csv_path)
        
        self._room = self._getRoom() 
        self._mtt = self._getMeetingTime()
        self._instrucs = self._getInstructor()
        self._course = self._getCourse()
        self._dept, self._noc = self._getDepartmentAndNumberOfClass()
        
       
    def _getRoom(self):
        rooms = []
        for i in range(len(self._room_df)):
            rooms.append(Room(self._room_df.iloc[i]['id'],
                              self._room_df.iloc[i]['seat_capacity']))
        return rooms

    def _getMeetingTime(self):
        meeting_times = []
        for i in range(len(self._mtt_df)):
            meeting_times.append(MeetingTime(self._mtt_df.iloc[i]['id'],
                                             self._mtt_df.iloc[i]['day'],
                                             self._mtt_df.iloc[i]['time']))
        return meeting_times

    def _getInstructor(self):
        instrucs = []
        for i in range(len(self._inst_df)):
            instrucs.append(Instructor(self._inst_df.iloc[i]['id'],
                                       self._inst_df.iloc[i]['professor']))
        return instrucs
    
    def _getCourse(self):
        courses = []
        for i in range(len(self._course_df)):
            courses.append(Course(self._course_df.iloc[i]['id'],
                                  self._course_df.iloc[i]['name'],
                                  self._instrucs[int(self._course_df.iloc[i]['instructor_id'])],
                                  self._course_df.iloc[i]['max_number_of_students']))
        return courses

    def _getDepartmentAndNumberOfClass(self):
        
        # Phase Department
        dept = []
        for i in range(len(self._dept_df)):
            course_id = str( self._dept_df.iloc[i]['course_id'] ).split(',') 
            courses = []
            for j in range(len(course_id)):
                courses.append( self._course[int( course_id[j] )] )
            dept.append(Department(self._dept_df.iloc[i]['name'], courses))
            courses = []
        
        # get Number of class
        noc = 0
        for i in range():
            noc += len(self._dept[i].getCourse())
        return dept, noc

    def getRoom(self):
        return self._room

    def getDepartment(self):
        return self._dept
    
    def getMeetingTime(self):
        return self._mtt
    
    def getNumberOfClass(self):
        return self._noc