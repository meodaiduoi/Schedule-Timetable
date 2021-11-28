from Data import Data
from FindSolution import FindSolution

import pandas as pd



def Main():
    '''
    Config:
    '''

    POPULATION_SIZE = 9
    NUMBER_OF_ELITE_SCHEDULES = 1
    TOURNAMENT_SELECTION_SIZE = 3
    MUTATION_RATE = 0.1

    data = Data('./data/Room.csv', './data/MeetingTime.csv',
                './data/Instructor.csv', './data/Department.csv',
                './data/Course.csv')

    find_solution = FindSolution(data, POPULATION_SIZE, NUMBER_OF_ELITE_SCHEDULES, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE)
    timetable = find_solution.getTimeTable()

    timetable.sort(key=lambda x: x.getMeetingTime().getId())

    for i in range(len(timetable)):
        print(timetable[i].__str__())

    return 0

if __name__ == '__main__':
    Main()