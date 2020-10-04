from random import sample
from typing import List
from typing import Tuple

from creator.individual import Individual


class Selector:

    def __init__(self, population: List[Individual]):
        self._population = population

    def select_pairs_of_parents(self, num_pairs: int) -> List[Tuple[Individual, Individual]]:
        return [self.select_parents() for _ in range(num_pairs)]

    def select_parents(self) -> Tuple[Individual, Individual]:
        
        return self._select_random_individuals(2)
        
        first_parent = self._select_parent()
        second_parent = self._select_parent()
        return first_parent, second_parent

    def select_best_individual(self):
        return self.select_best_individuals(1)[0]

    def select_best_individuals(self, num_individuals: int) -> List[Individual]:
        fitnesses = {i: individual.fitness for i, individual in enumerate(self._population)}
        sorted_fitnesses = dict(sorted(fitnesses.items(), key=lambda t: t[1]))
        best_individual_indices = list(sorted_fitnesses.keys())[-num_individuals:]
        return [self._population[i] for i in best_individual_indices]

    def _select_parent(self) -> Individual:
        # a, b = self._select_two_random_individuals()
        # c, d = self._select_two_random_individuals()
        
        selection = self._select_random_individuals(4)
        selection.sort(key=lambda x: x.fitness, reverse=True)
        return selection[0]
        
        # the_best = a if a.fitness >= b.fitness else b
        # the_best = c if c.fitness >= the_best.fitness else the_best
        # the_best = d if d.fitness >= the_best.fitness else the_best
        # return the_best
    
    def _select_random_individuals(self, k) -> Individual:
        return sample(self._population, k)

    def _select_two_random_individuals(self) -> Tuple[Individual, Individual]:
        first_individual = self._select_random_individual()
        second_individual = self._select_random_individual()
        return first_individual, second_individual

    def _select_random_individual(self) -> Individual:
        return sample(self._population, 1)[0]

    @staticmethod
    def _fitness(binary_string: str) -> int:
        return binary_string.count('1')
