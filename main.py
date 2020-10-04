import time
import numpy as np
from random import seed
from bisector.bisector import Bisector
from loading_indicator import LoadingIndicator


def main():
    """Finds the minimum population size to solve the onemax problem for a given string size."""
    string_size = prompt_for_string_size()
    A = np.zeros((10,), dtype=int)
    t0 = time.time()
    for i in range(10):
        A[i] = Bisector.find_minimum_population_size(string_size, seed_offset=i)
        print('A[{}] = {}'.format(i, A[i]))
    print('Avg:', np.mean(A))
    print('Std: {:.2f}'.format(np.std(A)))
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
