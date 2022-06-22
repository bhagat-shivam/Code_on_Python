import math

def perfect(x):
    s = int(math.sqrt(x))
    return s*s==x

def fibo(n):
    return perfect(5*n*n + 4) or perfect(5*n*n - 4)

for i in range(1,11):
        if (fibo(i) == True):
            print (i,"is fibo no")
        else:
                print(i,"is not fibo no")
    