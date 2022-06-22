def duplicate(input):
    return list(set([x for x in input if input.count(x) > 1]))

if __name__=='__main__':
    input = [1,2,3,1,2,4]
    print(duplicate(input))