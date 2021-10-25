'''
Deparment:

'''
class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def getName(self): return self._name
    def getCourse(self): return self._courses
'''
Meeting time

'''
class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def getId(self): return self._id
    def getTime(self): return self._time


'''
Course class

'''
class Course:
    def __init__(self, number, name, instructor, max_number_of_students):
        self.number = number
        self.name = name
        self.instructor = instructor
        self.max_students = max_number_of_students

    def __str__(self): return self.name

'''
Room:
    number
    seat_capacity
'''
class Room:
    def __init__(self, number, seat_capacity):
        self._number = number
        self._seet_capacity = seat_capacity

    def getNumber(self): return self._number
    def getSeatCapacity(self): return self._seet_capacity

'''
Instructor

'''
class Instructor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

'''
Class

'''
class Class:
    def __init__(self, id, department, course) -> None:
        self._id = id
        self._dept = department
        self._course = course
        self._instructor = None
        self._meeting_time = None
        self._room = None

    '''
    Accessor
    '''
    def getId(self): return self._id
    def getDept(self): return self._dept
    def getCourse(self): return self._course
    def getInstructor(self): return self._instructor
    def getMeetingTime(self): return self._meeting_time
    def getRoom(self): return self._room

    '''
    Mutator
    '''
    def setInstructor(self, instructor): self._instructor = instructor
    def setMeetingTime(self, meeting_time): self._meeting_time = meeting_time
    def setRoom(self, room): self._room = room

    '''
    toString():
    '''
    def __str__(self):
        return str(self.)
