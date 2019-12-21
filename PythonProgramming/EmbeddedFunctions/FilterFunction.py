filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8])

list1 = list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8]))

print(list1)

def primeNum(x):
    i = 2
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        while 1 < x:
            if x % i == 0:
                return False
            i += 1
        return True

print(primeNum(1))
print(primeNum(2))


# Calismadi
filter(primeNum, range(1,100))
list2 = list(filter(primeNum,range(1,100)))
print(list2)

