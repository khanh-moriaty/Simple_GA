import time
from random import seed
from bisector.bisector import Bisector
from loading_indicator import LoadingIndicator


def main():
    t0 = time.time()
    """Finds the minimum population size to solve the onemax problem for a given string size."""
    string_size = prompt_for_string_size()
    minimum_population_size = Bisector.find_minimum_population_size(string_size)
    print('Minimum population size: {}'.format(minimum_population_size))
    print(time.time()-t0)


def prompt_for_string_size() -> int:
    """Get string size from user."""
    string_size = 0
    while string_size < 1:
        try:
            string_size = int(input("String size: "))
        except ValueError:
            pass
    return string_size


if __name__ == '__main__':
    main()
