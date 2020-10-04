import unittest
from random import seed

from creator import Creator
from creator.individual import Individual


class TestCreator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        seed(1)
        cls._creator = Creator(population_size=6, string_size=5)

    def test_create_population(self):
        seed(1)
        population_size = 3
        creator = Creator(population_size=population_size, string_size=5)
        population = creator.create_population()
        expected_population = [Individual('00101'), Individual('11100'), Individual('10110')]

        self.assertEqual(population_size, len(population))
        self.assertEqual(expected_population, population)

    def test_create_individual(self):
        seed(1)
        expected_binary_string = Individual('00101')
        length = 5

        binary_string = self._creator._create_individual(length)

        self.assertEqual(length, len(binary_string))
        self.assertEqual(expected_binary_string, binary_string)

    def test_replace_population(self):
        seed(1)
        expected_new_population = [Individual('11101'), Individual('11001'),
                                   Individual('01100'), Individual('01100'),
                                   Individual('10110'), Individual('11001')]
        population = self._creator.create_population()
        new_population = self._creator._replace_population(population)
        self.assertEqual(expected_new_population, new_population)

    def test_evolve_population(self):
        seed(1)
        population = self._creator.create_population()
        evolved_population = self._creator.evolve_population(population)

        initial_average_fitness = self._creator.get_average_fitness(population)
        average_fitness_after_evolution = self._creator.get_average_fitness(evolved_population)
        self.assertGreater(average_fitness_after_evolution, initial_average_fitness)


if __name__ == '__main__':
    unittest.main()
