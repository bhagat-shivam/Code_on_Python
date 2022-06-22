def swap(list, post1, post2):

    list[post1], list[post2] = list[post2], list[post1]
    return list

list = [ 23, 65, 19, 90]
post1, post2 =1,3

print(swap(list, post1-1, post2-1))