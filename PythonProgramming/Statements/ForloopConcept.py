# in operators
# can be checked a value whether there is a list, tuple or string using in

print(5 in {1, 2, 3, 4})

print("hel" in "hello world")

print(10 in [1, 2, 3, 4])

print(not 4 in (1, 2, 3))

# for loop in list

list1 = [1, 2, 3, 4, 5, 6, 7]

for element in list1:
    print("Element", element)

# sum list using for

list2 = [1, 2, 3, 4, 5, 6, 7]
sumNumbers = 0
for element in list2:
    sumNumbers += element
print("Sum", sumNumbers)

list2 = [1, 2, 3, 4, 5, 6, 7]
sumNumbers = 0
for element in list2:
    sumNumbers += element
    print("Sum:  {} Element : {}".format(sumNumbers, element))
print("Sum: ", sumNumbers)

# Find even numbers

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in list3:
    if element % 2 == 0:
        print(element)

# String using for loop

st = "Python"
for character in st:
    print(character)

st = "Python"
for character in st:
    print(character * 3)

# tuple using for loop

tuple1 = (1, 2, 3, 4, 5, 6, 7)

for element in tuple1:
    print(element)

list4 = [(1, 2), (3, 4), (5, 6), (7, 8)]

for element in list4:
    print(element)

list5 = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (i, j) in list5:
    print(i, j)

for (i, j) in list5:
    print("i: {} j: {}".format(i, j))

list6 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for (i, j, k) in list6:
    print(i * j * k)

# Dictionary using for loop

# keys
art = {"one": 1, "two": 2, "three": 3, "four": 4}

for element in art.keys():
    print(element)

# values
art2 = {"one": 1, "two": 2, "three": 3, "four": 4}

for element in art2.values():
    print(element)

# items
art3 = {"one": 1, "two": 2, "three": 3, "four": 4}

for (i, j) in art3.items():
    print("Key:", i, "Value:", j)

