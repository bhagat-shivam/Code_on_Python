 # function for nth febonnaci number

def febo(n):
    if n<=0:
        print("incorrect input") #number can't be negative

        #first number is 0
    elif n==1:
            return 0
        # second numberis 1
    elif n==2:
            return 1
    else :
                return febo(n-1)+febo(n-2)

print(febo(10)) 


#2nd type method

''' fiboArr = [0,1]

def fibo(n):
    if n<0:
      print("incorrect input")
    elif n<len(fiboArr):
        return fiboArr[n-1]
    else:
            temp_fib = fibo(n-1)+fibo(n-2)
            fiboArr.append(temp_fib)
            return temp_fib

print(fibo(9)) '''


#3rd type method

''' def fibo(n):
    a=0
    b=1
    if n<1:
      print("incorrect")
    elif n==0:
        return a
    elif n==1:
        return b
    else: 
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b

print(fibo(9)) '''


# 4th method

''' def fibo(n):
    if n<=0:
        return "incorrect"
    data = [0,1]
    if n>2:
     for i in range(2,n):
            data.append(data[i-1] + data[i-2])

            return data[n-1]

print(fibo(9)) '''

