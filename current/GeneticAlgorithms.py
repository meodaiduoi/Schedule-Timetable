from Population import Population
from Schedule import Schedule
from Data import Data

import random as rnd

'''
Config:
'''
POPULATION_SIZE = 9
NUMBER_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1

'''

'''
class GeneticAlgorithms:
    '''

    '''
    def __init__(self, data: Data):
        self._data = data

    '''

    '''
    def _selectTournamentPopulation(self, pop: Population):
        tournament_pop = Population(0, self._data)
        for i in range(TOURNAMENT_SELECTION_SIZE):
            tournament_pop.getSchedule().append(pop.getSchedule()[rnd.randrange(0, POPULATION_SIZE)])
        tournament_pop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
        return tournament_pop

    '''

    '''
    def _mutatePopulation(self, pop: Population):
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutateSchedule(pop.getSchedule()[i])
        return pop

    '''

    '''
    def _mutateSchedule(self, mutate_schedule: Schedule):
        schedule = Schedule().initialize()
        for i in range(len(mutate_schedule.getClasses())):
            if(MUTATION_RATE > rnd.random()):
                mutate_schedule.getClasses()[i] = schedule.getClasses()[i]
        return mutate_schedule

    '''

    '''
    def _crossoverSchedule(self, schedule1: Schedule, schedule2: Schedule):
        crossover_schedule = Schedule.initialize()

    '''

    '''
    def _crossoverPopulation(self, pop: Population):
        crossover_pop = Population(0, self._data)
        for i in range(NUMBER_OF_ELITE_SCHEDULES):
            crossover_pop.getSchedule().append(pop.getSchedule()[i])

        for i in range(NUMBER_OF_ELITE_SCHEDULES,  POPULATION_SIZE):
            sche1 = self._selectTournamentPopulation(pop).getSchedule()[0]
            sche2 = self._selectTournamentPopulation(pop).getSchedule()[0]
            crossover_pop.getSchedule().append(self._crossoverSchedule(schedule1=sche1, schedule2=sche2))

        return crossover_pop

    '''

    '''
    def evolve(self, population: Population):
            return self._mutatePopulation(self._crossoverPopulation(population))