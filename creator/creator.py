from random import randint
from typing import List

from creator.breeder import Breeder
from creator.fitness_tracker import FitnessTracker
from creator.individual import Individual
from creator.selector import Selector
from creator.tournament import Tournament

class Creator:

    def __init__(self, population_size=10, string_size=5):
        self._population_size = population_size
        self._string_size = string_size

    def evolve_population(self, population: List[Individual]) -> List[Individual]:
        fitness_tracker = FitnessTracker(population)
        average_fitness = fitness_tracker.get_average_fitness()
        num_times_stable = 0
        num_generations = 1
        while num_times_stable <= 3:
            population = self._replace_population(population)
            fitness_tracker = FitnessTracker(population)
            new_average_fitness = fitness_tracker.get_average_fitness()
            num_times_stable += 1 if new_average_fitness == average_fitness else 0
            average_fitness = new_average_fitness
            num_generations += 1
        return population

    def create_population(self) -> List[Individual]:
        population = []
        for _ in range(self._population_size):
            individual = self._create_individual(self._string_size)
            population.append(individual)
        return population

    @staticmethod
    def _create_individual(size: int) -> Individual:
        binary_string = ''
        for _ in range(size):
            binary_string += str(randint(0, 1))
        return Individual(binary_string)

    def _replace_population(self, population: List[Individual]) -> List[Individual]:
        
        selector = Selector(population)
        breeder = Breeder(self._string_size)
        
        num_pairs = self._population_size // 2
        pairs_of_parents = selector.select_pairs_of_parents(num_pairs)
        
        offsprings = [None] * self._population_size
        for i, parents in enumerate(pairs_of_parents):
            children = breeder.breed(*parents)
            offsprings[2*i:2*i+2] = children
            
        if offsprings[-1] is None:
            offsprings[-1] = selector._select_random_individual().clone()
        
        assert len(population) == len(offsprings)
        
        pop = population[:] + offsprings[:]
        tournament = Tournament(pop, size=4)
        pop = tournament.fight(self._population_size)
        return pop
        
        # Select (N - 2) / 2 pairs of parents
        new_population = []
        selector = Selector(population)
        breeder = Breeder(self._string_size)
        num_pairs = int((self._population_size - 2) / 2)
        pairs_of_parents = selector.select_pairs_of_parents(num_pairs)

        # Breed N - 2 children
        for parents in pairs_of_parents:
            children = breeder.breed(*parents)
            new_population.extend(children)

        # Replace all but the 2 best parents
        two_best_parents = selector.select_best_individuals(2)
        new_population.extend(two_best_parents)

        return new_population

    @staticmethod
    def get_average_fitness(population: List[Individual]) -> float:
        fitness_tracker = FitnessTracker(population)
        return fitness_tracker.get_average_fitness()

    @staticmethod
    def select_best_individual(population: List[Individual]) -> Individual:
        selector = Selector(population)
        return selector.select_best_individual()
