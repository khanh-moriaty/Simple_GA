from random import shuffle
from typing import List
from typing import Tuple

from creator.individual import Individual

class Tournament:

    def __init__(self, population: List[Individual], size: int):
        # assert len(population) >= size, "Tournament size should not be less than population size!"
        self._population = population
        self._size = min(size, len(population))


    def fight(self, new_size) -> List[Individual]:
        new_population = [None] * new_size
        population = []
        index = 0
        for i in range(new_size):
            if index + self._size >= len(population):
                population = self._population
                shuffle(population)
                index = 0
            winner, population = self._fight(population, index)
            index += self._size
            new_population[i] = winner
        
        return new_population
    
    
    def _fight(self, population: List[Individual], index) -> Individual:
        fighters = population[index:index+self._size]
        return max(fighters, key=lambda x: x.fitness), population