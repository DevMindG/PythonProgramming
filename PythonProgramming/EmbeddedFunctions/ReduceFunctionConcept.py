from functools import reduce

def sum(x,y):
    return x + y
rd1 = reduce(sum, [12,18,20,10])
print(rd1)

rd2 = reduce(lambda x,y : x * y,[1,2,3,4,5,6])
print(rd2)

def maxFunc(x,y):
    if x > y:
        return x
    else:
        return y

print(maxFunc(3,4))

print(reduce(maxFunc,[-2,1,3,5,7,9]))

