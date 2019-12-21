with open("/Users/bobit/Desktop/info2.txt", "r") as file:
    print(file.tell())
    file.seek(3)
    print(file.tell())

with open("/Users/bobit/Desktop/info2.txt", "r") as file:
    file.seek(5)
    c = file.read(8)
    print(c)
    