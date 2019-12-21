list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
result = list()
while i < len(list1) and i < len(list2):
    result.append((list1[i], list2[i]))

    i += 1
print(result)

zip(list1,list2)
list3 = list(zip(list1,list2))
print(list3)

list4 = [1,2,3,4]
list5 = [5,6,7,8]
list6 = ["Python","Php","Java","Javascript","C"]

res = list(zip(list4,list5,list6))
print(res)

## Aynı anda iki liste üzerinde gezinmek
list4 = [1,2,3,4]
list6 = ["Python","Php","Java","Javascript"]

for i,j in zip(list4,list6):
    print("i:",i,"j:",j)

# Sözlükleri zipleyelim.
wrd1 = {"Apple":1, "Cherry":2, "Melon":3}
wrd2 = {"Zero":0, "One":1, "Two":2}

res2 = list(zip(wrd1,wrd2)) # Anahtarlar eşleşti.
print(res2)