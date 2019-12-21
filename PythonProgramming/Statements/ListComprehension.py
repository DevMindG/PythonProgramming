# While using list comprehension, we can create list with a shorter way

# Remember append
list1 = [1, 2, 3, 4, 5]

print(list1)

# Long way to create and append list

list3 = [1, 2, 3, 4, 5]

list4 = list()  # or list4 = [] both of them will create empty list

for i in list3:
    list4.append(i)  # values in list3 can be copied using for loop

print(list4)

# Using list comprehension

list5 = [1, 2, 3, 4, 5]

list6 = [i for i in list5]  # List Comprehension

print(list6)

# sample 2

list7 = [1, 2, 3, 4, 5]

list8 = [i * 2 for i in list7]  # List Comprehension

print(list8)

# sample 3

list9 = [(1, 2), (3, 4), (5, 6)]

list10 = [i * j for (i, j) in list9]  # List Comprehension

print(list10)

# sample 4

list11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list12 = [i for i in list11 if not (i == 4 or i == 9)]  # List Comprehension

print(list12)

# sample 5

s = "Python"

list13 = [i * 3 for i in s]  # List Comprehension

print(list13)

# nested list sample

list14 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
list15 = [x for i in list14 for x in i]
print(list15)

