import unittest

from creator.fitness_tracker import FitnessTracker
from creator.individual import Individual


class TestFitnessTracker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        population = [Individual('10101'), Individual('1100'), Individual('01111')]
        cls._fitness_tracker = FitnessTracker(population)

    def test_average_fitness(self):
        expected_average_fitness = 3
        self.assertEqual(expected_average_fitness, self._fitness_tracker.get_average_fitness())


if __name__ == '__main__':
    unittest.main()
