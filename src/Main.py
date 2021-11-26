from Data import Data
from GeneticAlgorithms import GeneticAlgorithms
from Schedule import Schedule
from Population import Population
from ClassScheduleDT import *


def Main():
    '''
    Config:
    '''
    
    POPULATION_SIZE = 9
    NUMBER_OF_ELITE_SCHEDULES = 1
    TOURNAMENT_SELECTION_SIZE = 3
    MUTATION_RATE = 0.1
    
    # data = Data('./data/Room.csv', './data/MeetingTime.csv',
    #             './data/Instructor.csv', './data/Department.csv',
    #             './data/Course.csv')
    
    data = Data('./data2/Room.csv', './data2/MeetingTime.csv',
                './data2/Instructor.csv', './data2/Department.csv',
                './data2/Course.csv')
    
    generticAlogrithm = GeneticAlgorithms(data)
    population = Population(POPULATION_SIZE, data)
    
    # print(data.getRoom()[0].getCapacity())
    
    generation = 0
    
    while (population.getSchedule()[0].getFitness() != 1.0):
        generation += 1
        print('Generation: ', generation)
        population = generticAlogrithm.evolve(population)
    
    return 0


if __name__ == '__main__':
    Main()