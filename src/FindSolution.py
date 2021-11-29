from Data import Data
from GeneticAlgorithms import GeneticAlgorithms
from Population import Population
from ClassScheduleDT import *

class FindSolution():
    def __init__(self, data: Data, population_size, number_of_elite_schedules, tournament_selection_size, mutation_rate):
        self._data = data
        self._POPULATION_SIZE = population_size
        self._NUMBER_OF_ELITE_SCHEDULES = number_of_elite_schedules
        self._TOURNAMENT_SELECTION_SIZE = tournament_selection_size
        self._MUTATION_RATE = mutation_rate

        # generation and sorted solution by time
        self._generation = []
        self._solution = self._find()
        self._solution.sort(key=lambda x: x.getMeetingTime().getId())

    def _find(self):

        generticAlogrithm = GeneticAlgorithms(self._data, self._POPULATION_SIZE, self._NUMBER_OF_ELITE_SCHEDULES, self._TOURNAMENT_SELECTION_SIZE, self._MUTATION_RATE)
        # Get first Sample to cross
        population = Population(self._POPULATION_SIZE, self._data)

        generation = 0
        while (population.getSchedule()[0].getFitness() != 1.0):
            population = generticAlogrithm.evolve(population)
            population.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
            self._generation.append(population.getSchedule()[0].getClasses())

            generation += 1
            print('Generation:', generation, 'Fitness:', population.getSchedule()[0].getFitness())

        # Sort the solution by meeting time ID
        return population.getSchedule()[0].getClasses()

    def getTimeTable(self):
        return self._solution

    def getGeneration(self):
        return self._generation

    def getGenerationLen(self):
        return len(self._generation)

    def __str__(self) -> str:
        return str()