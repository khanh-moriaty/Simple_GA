from typing import List

from creator import Creator
from creator.individual import Individual

from random import seed

class Bisector:

    @classmethod
    def _find_upperbound(cls, string_size, seed_offset=0, num_runs=10):
        upper_bound = 1
        success = False
        while not success:
            upper_bound = 2 * upper_bound
            if upper_bound > 8192: return -1
            success = 0
            creator = Creator(population_size=upper_bound, string_size=string_size)
            for i in range(num_runs):
                seed(19520624 + 10*i + seed_offset)
                population = creator.create_population()
                evolved_population, evaluations = creator.evolve_population(population)
                if cls._found_global_optimum(creator, evolved_population, string_size):
                    success += 1
        return upper_bound

    @classmethod
    def find_minimum_population_size(cls, string_size, seed_offset=0, num_runs=10) -> int:
        upper_bound = cls._find_upperbound(string_size, seed_offset=seed_offset)
        if upper_bound == -1: return -1
        lower_bound = upper_bound // 2
        found_upper_bound = False
        found_global_optimum_count = 0
        res = -1, -1
        # while lower_bound != upper_bound or found_global_optimum_count != num_runs:
        while lower_bound <= upper_bound:
            population_size = (lower_bound + upper_bound) // 2
            found_global_optimum_count = 0
            
            creator = Creator(population_size=population_size, string_size=string_size)

            average_number_of_evaluations = 0
            for i in range(num_runs):
                # print(population_size, i)
                seed(19520624 + 10*i + seed_offset)
                population = creator.create_population()
                evolved_population, evaluations = creator.evolve_population(population)
                average_number_of_evaluations += evaluations / 10
                if cls._found_global_optimum(creator, evolved_population, string_size):
                    found_global_optimum_count += 1

            if found_global_optimum_count:
                res = population_size, average_number_of_evaluations
                upper_bound = population_size - 1
            else:
                lower_bound = population_size + 1

            # if found_global_optimum_count > 0:  # Found global optimum.
            #     upper_bound = population_size
            #     if not found_upper_bound:
            #         lower_bound = int(population_size / 2)
            #     population_size = cls._midpoint(lower_bound, upper_bound)
            #     found_upper_bound = True
            # else:  # Failed to find global optimum 5/5 times
            #     if lower_bound == upper_bound:  # Lower and upper bound converged
            #         # Increment population size until it succeeds 5/5 times
            #         population_size += 2
            #         lower_bound = population_size
            #         upper_bound = population_size
            #     elif found_upper_bound:  # Found upper bound and failed.
            #         # Increase lower bound and population size.
            #         population_size = cls._midpoint(lower_bound, upper_bound)
            #         lower_bound = population_size
            #         if upper_bound - lower_bound == 2:
            #             lower_bound += 2
            #     else:  # Failed without finding upper bound.
            #         population_size *= 2  # Double population size
        return res

    @staticmethod
    def _found_global_optimum(creator: Creator, population: List[Individual], string_size: int):
        best_individual = creator.select_best_individual(population)
        return best_individual.fitness == string_size

    @classmethod
    def _midpoint(cls, a: int, b: int) -> int:
        midpoint = round((a + b) / 2)
        return midpoint if cls._is_even(midpoint) else midpoint - 1

    @staticmethod
    def _is_even(num: int) -> bool:
        return num % 2 == 0
