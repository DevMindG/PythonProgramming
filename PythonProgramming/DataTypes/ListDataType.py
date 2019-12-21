
my_list = [23, "hello", 34.12, "Bob"]
print(my_list)
print(type(my_list))

# empty list

myList = []
print(myList)

# length list
myList2 = [1, 2, 3, 4, 5, 6, 7]
print(len(myList2))

# To print every character separately
mylist3 = list("helloworld")
print(mylist3)

# to get specific character index
print(mylist3[3])

# parcalama

print(mylist3[4:])
print(mylist3[:5])
print(mylist3[::-1])

# You can sum all list

myList4 = [1, 2, 3]
myList5 = [4, 5, 6]
myList6 = myList4 + myList5
print(myList6)

# you can multiplication

print(myList6 * 2)

print(myList4)
ad = myList4[1] = 4
print(ad)
print(myList4)

# methods in list

# append function to add new value

myList4.append(55)
print(myList4)

myList4.append(78)
print(myList4)

# pop function to drop a value from the list it works according to index

myList4.pop(4)
print(myList4)

# sort function to order the list siralama

myList8 = [1, 3, 100, 6, 8, 9, 11]
myList8.sort()
print(myList8)

# reverse sort
myList9 = [1, 100, 99, 45, 101, 10]
myList9.sort(reverse=True)
print(myList9)

# nested list

myList10 = [[1, 2], [3, 4], [5, 6]]
print(myList10)
print(myList10[1])  # to go specific list
print(myList10[1][1]) # to go first list first value from list
