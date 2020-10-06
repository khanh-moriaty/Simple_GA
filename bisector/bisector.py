from typing import List

from creator import Creator
from creator.individual import Individual

from random import seed
from multiprocessing import Pool
from itertools import repeat

class Bisector:

    @classmethod
    def _simulate_population(cls, i, seed_offset, population_size, string_size):
        seed(19520624 + 10*i + seed_offset)
        creator = Creator(population_size=population_size, string_size=string_size)
        
        population = creator.create_population()
        evolved_population, evaluations = creator.evolve_population(population)
        
        success = False
        if cls._found_global_optimum(creator, evolved_population, string_size):
            success = True
            
        return success, evaluations

    @classmethod
    def _find_upperbound(cls, string_size, seed_offset=0, num_runs=10):
        upper_bound = 1
        while True:
            upper_bound = 2 * upper_bound
            if upper_bound > 8192: return -1
            with Pool(10) as pool:
                res = pool.starmap(cls._simulate_population, zip(range(num_runs), repeat(seed_offset), repeat(upper_bound), repeat(string_size)))
            success, _ = zip(*res)
            if any(success):
                break
        return upper_bound

    @classmethod
    def find_minimum_population_size(cls, string_size, seed_offset=0, num_runs=10) -> int:
        upper_bound = cls._find_upperbound(string_size, seed_offset=seed_offset)
        if upper_bound == -1: return -1, -1
        lower_bound = upper_bound // 2
        found_upper_bound = False
        found_global_optimum_count = 0
        res = -1, -1
        # while lower_bound != upper_bound or found_global_optimum_count != num_runs:
        while lower_bound <= upper_bound:
            population_size = (lower_bound + upper_bound) // 2
            found_global_optimum_count = 0
            
            

            with Pool(num_runs) as pool:
                simulation_results = pool.starmap(cls._simulate_population, zip(range(10), repeat(seed_offset), repeat(population_size), repeat(string_size)))
            found_global_optimum_count, number_of_evaluations = zip(*simulation_results)
            average_number_of_evaluations = sum(number_of_evaluations) / num_runs

            if any(found_global_optimum_count):
                res = population_size, average_number_of_evaluations
                upper_bound = population_size - 1
            else:
                lower_bound = population_size + 1

        return res

    @classmethod
    def _found_global_optimum(cls, creator: Creator, population: List[Individual], string_size: int):
        best_individual = creator.select_best_individual(population)
        return best_individual.fitness == string_size
