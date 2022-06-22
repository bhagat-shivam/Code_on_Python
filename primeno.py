def prime(x,y):
    primelist = []
    for i in range(x,y):
     if i==0 or i==1:
        continue
    else :
        for j in range(2, int(i/2)+1):
            if i%j ==0:
                break
            else:
                primelist.append(i)
                return primelist

starting_range = 2
ending_range = 7
first = prime(starting_range, ending_range)
if len(first) == 0:
     print("there is no prime number")
else :
     print("the prime number is ", first)