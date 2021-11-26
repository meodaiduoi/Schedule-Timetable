import random as rnd

from Data import Data
from ClassScheduleDT import *

'''
Schedule:

'''
class Schedule:
    def __init__(self, data: Data):
        self._data = data
        self._classes: list[Class] = []
        self._conflict = 0
        self._fitness = -1
        self._class_number = 0
        self._is_fitness_changed = True

    def getClasses(self):
        self._is_fitness_changed = True
        return self._classes

    def getNumberOfConflicts(self):
        return self._conflict

    def getFitness(self):
        if (self._is_fitness_changed == True):
            self._fitness = self.calculateFitness()
            self._is_fitness_changed == False
        return self._fitness

    def calculateFitness(self):
        self._conflict = 0
        classes: list[Class] = self.getClasses()

        for i in range(0, len(classes)):
            if (classes[i].getRoom().getCapacity() < classes[i].getCourse().getMaxStudent()):
                self._conflict +=1
                # print("Room Conflic")

            for j in range(0, len(classes)):
                if (j >=i):
                    if (classes[i].getMeetingTime() == classes[j].getMeetingTime() and
                        classes[i].getId() != classes[j].getId()):
                        # print("Class Conflic")
                        if (classes[i].getRoom() == classes[j].getRoom()):
                            self._conflict += 1
                            # print("Room Conflic")
                        if (classes[i].getInstructor() ==  classes[j].getInstructor()):
                            self._conflict += 1
                            # print("Instruct Conflic")
        return 1 / (1.0 * self._conflict +1)

    def initialize(self):

        depts: list[Department] = self._data.getDepartment()

        for i in range(0, len(depts)):
            course: list[Course] = depts[i].getCourse()
            for j in range(0, len(course)):
                new_class = Class(self._class_number, depts[i], course[j])
                self._class_number += 1

                new_class.setRoom(self._data.getRoom()[rnd.randrange(0, len(self._data.getRoom()))])
                new_class.setMeetingTime(self._data.getMeetingTime()[rnd.randrange(0, len(self._data.getMeetingTime()))])
                new_class.setInstructor(course[j].getInstructor()[rnd.randrange(0, len(course[j].getInstructor()))])

                self._classes.append(new_class)

        return self