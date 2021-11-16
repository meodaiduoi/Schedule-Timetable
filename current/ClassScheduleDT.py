'''
Date:
'''
class Date:
    def __init__(self, day, time):
        self._day
        self._time

    def getDate(self):
        return self._day, self._time

    def __str__(self):
        return str('Day: ' + self._day + ' Time' + self._time)

'''
Meeting time

'''
class MeetingTime:
    def __init__(self, id, time: Date):
        self._id = id
        self._time = time

    def getId(self): return self._id
    def getTime(self): return self._time

'''
Room:
    number
    seat_capacity
'''
class Room:
    def __init__(self, id, seat_capacity):
        self._id = id
        self._seet_capacity = seat_capacity

    def getId(self): return self._id
    def getCapacity(self): return self._seet_capacity

'''
Instructor

'''
class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
     
'''
Course:

'''
class Course:
    def __init__(self, id, name: str, instructor: Instructor, max_number_of_students: int):
        self._number = id
        self._name = name
        self._instructor = instructor
        self._max_students = max_number_of_students

    def getMaxStudent(self): return self._max_students
    def getInstructor(self): return self._instructor
    def getName(self): return self._name
    def __str__(self): return self.name
    
'''
Deparment:

'''
class Department:
    def __init__(self, name: str, course):
        self._name = name
        self._course = course

    def getName(self): return self._name
    def getCourse(self): return self._course

'''
Class:
After Scheduling we have classes
'''
class Class:
    def __init__(self, id, department: Department, course: Course) -> None:
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
        return str(self._dept.getName()) + ',' +str(self._course.getNumber()) + ',' + \
            str(self._room.getNumber()) + ',' + str(self._instructor.getId()) + ',' + str(self._meeting_time.getId())
       