from Population import Population
from Schedule import Schedule
from Data import Data

import random as rnd

'''
Config:

POPULATION_SIZE = 9
NUMBER_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1
'''


'''

'''
class GeneticAlgorithms:
    '''

    '''
    def __init__(self, data: Data, population_size= 9, number_of_elite_schedules= 1, tournament_selection_size= 3, muatation_rate= 0):
        self._data = data
        self._POPULATION_SIZE = population_size
        self._NUMBER_OF_ELITE_SCHEDULES = number_of_elite_schedules
        self._TOURNAMENT_SELECTION_SIZE = tournament_selection_size
        self._MUTATION_RATE = muatation_rate

    '''

    '''
    def _selectTournamentPopulation(self, pop: Population):
        tournament_pop = Population(0, self._data)
        for _ in range(self._TOURNAMENT_SELECTION_SIZE):
            tournament_pop.getSchedule().append(pop.getSchedule()[rnd.randrange(0, self._POPULATION_SIZE)])
        tournament_pop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
        return tournament_pop
    
    '''
    25:06
    '''
    def _crossoverSchedule(self, schedule1: Schedule, schedule2: Schedule):
        crossover_schedule: Schedule = Schedule(self._data).initialize()
        for i in range(0, len(crossover_schedule.getClasses())):
            if (rnd.random() > 0.5):
                crossover_schedule.getClasses()[i] = schedule1.getClasses()[i]
            else:
                crossover_schedule.getClasses()[i] = schedule2.getClasses()[i]
        return crossover_schedule          

    '''
    use:
    _crossoverSchedule
    _selectTournamentPopulation
    '''
    def _crossoverPopulation(self, pop: Population):
        crossover_pop = Population(0, self._data)
        for i in range(self._NUMBER_OF_ELITE_SCHEDULES):
            crossover_pop.getSchedule().append(pop.getSchedule()[i])

        for i in range(self._NUMBER_OF_ELITE_SCHEDULES, self._POPULATION_SIZE):
            sche1 = self._selectTournamentPopulation(pop).getSchedule()[0]
            sche2 = self._selectTournamentPopulation(pop).getSchedule()[0]
            crossover_pop.getSchedule().append(self._crossoverSchedule(schedule1=sche1, schedule2=sche2))

        return crossover_pop
    
    '''

    '''
    def _mutateSchedule(self, mutate_schedule: Schedule):
        schedule = Schedule(self._data).initialize()
        for i in range(len(mutate_schedule.getClasses())):
            if(self._MUTATION_RATE > rnd.random()):
                mutate_schedule.getClasses()[i] = schedule.getClasses()[i]
        return mutate_schedule

    '''
    use: _mutateSchedule()

    '''
    def _mutatePopulation(self, pop: Population):
        for i in range(self._NUMBER_OF_ELITE_SCHEDULES, self._POPULATION_SIZE):
            self._mutateSchedule(pop.getSchedule()[i])
        return pop
    
    '''

    '''
    def evolve(self, population: Population):
            return self._mutatePopulation(self._crossoverPopulation(population))