list1 = ["Apple", "Cherry", "Ananas", "Kiwi"]

# sonucu [(0,'Apple'),(1,'Cherry'),(2,'Ananas'),(3,'Kiwi')] yapmak istiyoruz.

res = list()

i = 0

for a in list1:
    res.append((i, a))
    i += 1
print(res)

list1 = ["Apple","Cherry","Ananas","Kiwi"]
tr = list(enumerate(list1))
print(tr)

list3 = ["a", "b", "c", "d", "e", "f", "g"]

for index, element in enumerate(list3):
    if index % 2 == 0:
        print("Element: ", element)
