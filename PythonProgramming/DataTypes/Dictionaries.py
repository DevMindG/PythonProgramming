# in dictionary, there is key and value relationship like map in java
# dictionary is dynamic which means it is changeable

# how to create dictionary
myDic = {"one": 1, "two": 2, "three": 3, "four": 4}
print(myDic)

# how to reach a value from dictionary and how to add a value
print(myDic["one"])

myDic["five"] = 5
print(myDic)

myDic2 = {"one": [1, 2, 3, 4], "two": 15}
print(myDic2["one"])

a = {"one": [1, 2, 3, 4], "two": [[1, 2], [3, 4], [5, 6]], "three": 15}
print(a)

print(a["two"])

print(a["two"][1][1])

a["three"] += 5
print(a["three"])

print(a)

# we can add a value dynamically
a1 = {"one": 1, "two": 2, "three": 3, "four": 4}

print(a1)

# nested dictionary

b = {"numbers": {"one": 1, "two": 2, "three": 3}, "fruits": {"cherry": "summer", "orange": "winter", "plum": "summer"}}

print(b["numbers"]["one"])

print(b["fruits"]["cherry"])

# methods in dictionary

newDic = {"bir": 1, "iki": 2, "üç": 3}

# values return  a list from dictionary values (sozlugun degerlerini liste olarak doner)
print(newDic.values())

# keys return a list from dictionary keys
print(newDic.keys())

# items return a list keys and values together from dictionary
print(newDic.items())