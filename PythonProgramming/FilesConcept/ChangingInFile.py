with open("/Users/bobit/Desktop/info2.txt", "r+") as file:
    print(file.read())

with open("/Users/bobit/Desktop/info2.txt", "r+") as file:
    file.seek(10)
    file.write("Deneme")

with open("/Users/bobit/Desktop/info2.txt", "r+") as file:
    print(file.read())

with open("/Users/bobit/Desktop/info2.txt", "a") as file:
    file.write("Michael Jackson")

with open("/Users/bobit/Desktop/info2.txt", "r+") as file:
    print(file.read())
    