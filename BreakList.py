'''li = [1,2,3,4,5,6,7]
n = 4
x = [li[i:i]+ n for i in range(0, len(li),n)]
print(x)'''

list = [1,2,3,4,5,6,7]
n = 4
final = [list[i * n:(i+1) * n] for i in range((len(list) + n-1)// n)]
print(final)