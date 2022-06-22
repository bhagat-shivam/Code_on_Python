def cloning(li):
    li_copy = list(li)
    return li_copy

li = [1,2,3,4,5]
li2 = cloning(li)
print("original list:", li)
print("after cloning:", li2)