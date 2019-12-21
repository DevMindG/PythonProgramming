"""
def sum(a, b, c):
    print("The sum of numbers: ", a + b + c)


def multiplyTwo(a):
    print("Multiply with two: ", a * 2)


sum(3, 4, 5)
multiplyTwo(4)

"""


# ========================================

def sum1(a, b, c):
    return a + b + c


def multiplyTwo(a):
    return a * 2


print(sum1(2, 3, 4))
sumOfNumbers = sum1(2, 3, 4)
print(multiplyTwo(sumOfNumbers))


def sum3(a, b, c):
    print("Sum of numbers: ")
    return a + b + c


print(sum3(1, 1, 1))
