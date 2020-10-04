import unittest
from random import seed

from creator.breeder import Breeder
from creator.individual import Individual


class TestBreeder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._breeder = Breeder(5)

    def test_breed(self):
        seed(10)  # Seed with 10 to apply uniform crossover operator
        expected_children = (Individual('01010'), Individual('00110'))
        children = self._breeder.breed(Individual('01010'), Individual('00111'))
        self.assertEqual(expected_children, children)

    def test_uniform_crossover(self):
        seed(1)
        expected_children = (Individual('10001'), Individual('01110'))
        children = self._breeder._uniform_crossover(Individual('01011'), Individual('10100'))
        self.assertEqual(expected_children, children)

    def test_mutate(self):
        seed(1)
        expected_child = Individual('00100')
        child = self._breeder._mutate(Individual('10100'))
        self.assertEqual(expected_child, child)


if __name__ == '__main__':
    unittest.main()
