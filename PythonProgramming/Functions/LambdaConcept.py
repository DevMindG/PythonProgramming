list1 = [1, 2, 3, 4, 5, 6]

list2 = [i * 2 for i in list1]
print(list2)


def multiplyTwo(x):
    return x * 2

print(multiplyTwo(3))

multiply = lambda x : x * 2
print(multiply(5))

def sum(x,y,z):
    return x+y+z
print(sum(10,20,30))

numberOfSum = lambda x,y,z : x + y + z
print(numberOfSum(10,30,40))

def reverseString(s):
    return s[::-1]
print(reverseString("Python Programming"))

reverseStr = lambda s : s[::-1]
print(reverseStr("Python"))