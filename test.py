from random import seed

from creator.individual import Individual
from creator.tournament import Tournament
from creator.creator import Creator
from creator.fitness_tracker import FitnessTracker

if __name__ == '__main__':
    seed(42)
    creator = Creator(population_size=100, string_size=100)
    population = creator.create_population()
    print(population)
    tracker = FitnessTracker(population)
    print(tracker.get_average_fitness())
    population = creator.evolve_population(population)
    print(population)
    tracker = FitnessTracker(population)
    print(tracker.get_average_fitness())