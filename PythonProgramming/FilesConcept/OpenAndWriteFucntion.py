open("info.txt", "w")

file = open("info.txt", "w")

file.close()

file = open("/Users/bobit/Desktop/info2.txt", "w")


file.write("Bob\n")
file.close()

file = open("/Users/bobit/Desktop/info2.txt", "a")
file.write("Robert Akman")
file.close()