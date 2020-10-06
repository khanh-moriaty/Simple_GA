import numpy as np

from creator import fitness_functions

class Individual:
    """Wrapper class for an individual in a population."""

    def __init__(self, binary_string, fitness_function=fitness_functions.OneMax):
        """Construct an individual of a population
        :param binary_string: Binary string representing a member from a population.
        """
        self.binary_string = binary_string
        self.fitness_function = fitness_function

    @property
    def fitness(self):
        return self.fitness_function(self.binary_string)

    def clone(self):
        return Individual(self.binary_string)

    def __repr__(self):
        return "<Individual '{}'>".format(self.binary_string)

    def __str__(self):
        return "<Individual '{}'>".format(self.binary_string)

    def __eq__(self, other):
        return isinstance(other, Individual) and self.binary_string == other.binary_string

    def __getitem__(self, key):
        return self.binary_string[key]

    def __iadd__(self, other):
        assert isinstance(other, str)
        return Individual(self.binary_string + other)

    def __add__(self, other):
        return Individual(self.binary_string + other.binary_string)

    def __radd__(self, other):
        return Individual(other.binary_string + self.binary_string)

    def __len__(self):
        return len(self.binary_string)
