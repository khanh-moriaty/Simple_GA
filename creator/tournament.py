from random import shuffle
from typing import List
from typing import Tuple

from creator.individual import Individual

class Tournament:

    def __init__(self, population: List[Individual], size: int):
        assert len(population) >= size, "Tournament size should not be less than population size!"
        self._population = population
        self._size = size


    def fight(self, new_size) -> List[Individual]:
        new_population = [None] * new_size
        index = 0
        population = []
        for i in range(new_size):
            if len(population) < self._size:
                population = self._population.copy()
                shuffle(population)
            winner, population = self._fight(population)
            new_population[i] = winner
        
        return new_population
    
    
    def _fight(self, population: List[Individual]) -> Individual:
        fighters = population[:self._size]
        population = population[self._size:]
        return max(fighters, key=lambda x: x.fitness), population