def countX(st, x):
    return st.count(x)

st = [1,2,3,4,3,2,5,6,4,2]
x = 3
print('{} has occured {} times'.format(x, countX(st, x)))


# 2nd method

'''from collections import Counter


l = [1,1,2,2,3,3,4,4]
x = 3
d = Counter(l)
print('{} has occured {} times'.format(x, d[x]))'''