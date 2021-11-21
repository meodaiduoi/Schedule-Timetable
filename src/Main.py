from Data import Data
from GeneticAlgorithms import GeneticAlgorithms
from Schedule import Schedule
from Population import Population


def Main():
    # '''
    # Config:
    # '''
    
    # POPULATION_SIZE = 9
    # NUMBER_OF_ELITE_SCHEDULES = 1
    # TOURNAMENT_SELECTION_SIZE = 3
    # MUTATION_RATE = 0.1
    
    # data = Data('./data/Room.csv', './data/MeetingTime.csv/'
    #             './data/Instructor.csv', './data/Department.csv'
    #             './data/Course.csv')
    
    # generticAlogrithm = GeneticAlgorithms(data)
    # population: Population = generticAlogrithm.evolve()
    # schedule = population.getSchedule()
    
    data = Data('./data/Room.csv', './data/MeetingTime.csv',
                './data/Instructor.csv', './data/Department.csv',
                './data/Course.csv')
    return 0

if __name__ == '__main__':
    Main()