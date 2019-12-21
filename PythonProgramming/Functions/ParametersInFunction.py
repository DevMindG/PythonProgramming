def hello(name):
    print("Name: ", name)


hello("Robert")


# default parameter

def hello(name="You didn't enter any name"):
    print("Name: ", name)


hello()
hello("Richard")


def showInfo(name="no info", lastName="no info", phone="no info"):
    print("Name:", name, "Last name:", lastName, "Phone:", phone)


showInfo("Ricahrd", "Larry", "2019148199")
showInfo()

print("Robert", "Boby", "Larry", sep="/")


def sum(*a):
    print(a)


sum(1, 2, 3)
sum(1, 2, 3, 4, 5)

# we can put parameters using * sign and can be put different numbers of value
def sum2(*a):
    sum3 = 0
    for i in a:
        sum3 += i
    print(sum3)


sum2(4, 1, 1)
