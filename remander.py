from functools import reduce
from math import reduce

def find_remainder(arr,n):
    sum = reduce(lambda x,y: x*y,arr)
    remainder = sum%n
    print(remainder)

    arr = [100,10,5,25,35,14]
    n = 11
    find_remainder(arr,n)