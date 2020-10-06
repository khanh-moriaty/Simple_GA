import time
import numpy as np
from random import seed
from datetime import timedelta
from bisector.bisector import Bisector


def main():
    """Finds the minimum population size to solve the onemax problem for a given string size."""
    # string_size = prompt_for_string_size()
    # print()
    # bisection(string_size)
    
    for i in [10, 20, 40, 80, 160]:
        bisection(i)
    
def bisection(string_size):
    print('###################### string_size = {} ######################\n'.format(string_size))
    t0 = time.time()
    A = [0] * 10
    B = [0] * 10
    for i in range(10):
        A[i], B[i] = Bisector.find_minimum_population_size(string_size, seed_offset=i)
        print('Min[{}] = {}\t|| Eval[{}] = {:.1f}'.format(i, A[i], i, B[i]))
    C = [(x, y) for (x, y) in zip(A, B) if x != -1]
    print()
    if len(C) == 0:
        print('No stats!')
    else:
        A, B = zip(*C)
        print('Avg_A: {:.2f}'.format(np.mean(A)))
        print('Std_A: {:.2f}\n'.format(np.std(A)))
        print('Avg_B: {:.2f}'.format(np.mean(B)))
        print('Std_B: {:.2f}\n'.format(np.std(B)))
    
    t0 = int(round(time.time()-t0))
    print('Running time: {}\n'.format(timedelta(seconds=t0)))


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
