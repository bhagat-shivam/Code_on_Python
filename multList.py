from cgitb import reset
from unittest import result


''' def mul(list):
    result = 1
    for x in list:
        result = result * x
    return result

l1 = [1,2,3]
print(mul(l1)) '''

#2nd method of multiply list

import math
li =[1,2,3,4,5]

result = math.prod(li)
print(result)