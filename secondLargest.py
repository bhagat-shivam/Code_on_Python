''' li = [1,2,5,4,3]
print("second largest: ", sorted(li)[-2]) '''



#2nd method of largest 2nd number

li1 = [1,2,3,4,5]

li2 = list(set(li1))

li2.sort()
print("second largest", li2[-2])