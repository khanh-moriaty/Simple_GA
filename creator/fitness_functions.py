import numpy as np

def OneMax(binary_string):
    count = binary_string.count('1')
    return count
    
def Trap(binary_string, k=5):
    res = 0
    for i in range(len(binary_string) // k):
        count = binary_string[k*i:k*(i+1)].count('1')
        if count == k: res += k
        else: res += k - count - 1
    return res