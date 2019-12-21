file = open("/Users/bobit/Desktop/info2.txt", "r")
file.close()

file = open("/Users/bobit/Desktop/info2.txt", "r")

"""
for i in file:
    print(i, end = "")
file.close()
"""


# print(file.read())

file = open("/Users/bobit/Desktop/info2.txt", "r")
print(file.readline())
file.close()
