''' r = [1,2,3,4,5]
l = []

for i  in r:
    l.insert(0,i)
    print(l) '''

# 2nd method to reverse a list

def rev(r):
    r.reverse()
    return r

r = [1,2,3,4,5]
print(rev(r))