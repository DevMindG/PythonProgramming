# Creating function
def hello():
    print("How are you bro..")
    print("Are you ok?")


# Calling function
hello()


# Parameters in Function

def hello(name):
    print("Name: ", name)


hello("Bob")

hello("Liza")


def sum(a, b, c):
    print("The sum of the numbers: ", a + b + c)


sum(2, 3, 4)


def factorial(number):
    factorial1 = 1
    if number == 0 or number == 1:
        print("Factorial", factorial1)
    else:
        while number >= 1:
            factorial1 *= number
            number -= 1
        print("Factorial", factorial1)


factorial(6)
factorial(5)
factorial(2)
