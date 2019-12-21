def double(x):
    return x * 2

map(double,[1,2,3,4,5,6,7])

list1 = list(map(double,[1,2,3,4,5,6,7]))
print(list1)

list2 = list(map(lambda x : x ** 2,(1,2,3,4,5,6,7,8,9,10)))
print(list2)

list3 = [1,2,3,4,5]
list4 = [6,7,8,9,10]
list5 = [11,12,13,14,15]

list6 = list(map(lambda x,y : x*y, list3,list4))
print(list6)

list7 = list(map(lambda x,y,z : x*y*z, list3,list4, list5))
print(list7)

