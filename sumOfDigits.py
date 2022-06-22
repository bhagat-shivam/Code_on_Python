li = [12,67,98,34]
print(li)

res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), li))

print(res)