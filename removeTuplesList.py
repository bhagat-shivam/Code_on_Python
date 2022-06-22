def remove(tuples):
    tuples = filter(None, tuples)
    return tuples

tuples = [(), ('ram', '15','8'),(),('laxman','sita')]
print(remove(tuples))