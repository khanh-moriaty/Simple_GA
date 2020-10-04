from typing import List

from .individual import Individual


class FitnessTracker:
    def __init__(self, population: List[Individual]):
        self._population = population

    def get_average_fitness(self) -> float:
        fitnesses = [individual.fitness for individual in self._population]
        return sum(fitnesses) / float(len(self._population))
