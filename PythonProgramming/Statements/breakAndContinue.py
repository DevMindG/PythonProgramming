# break

i = 0  # break kullanmaya çalışalım.

while i < 20:
    print(i)
    if i == 10:
        break
    i += 1

# break with for loop

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list1:
    if i == 5:
        break
    print(i)

# break while

""" 
while True:
    name = input("Your name (Please enter q to exit system):")
    if name == "q":
        print("System is shutdown")
        break
    print(name)
"""
# continue

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list2:
    if i == 3 or i == 5:
        continue
    print("i:", i)

# continue with infinity

""" 
i = 0

while i < 10:

    if i == 2:
        continue

    print(i)
    i += 1
"""
i = 0

while i < 10:

    if i == 2:
        i += 1
        continue

    print("i:", i)
    i += 1


