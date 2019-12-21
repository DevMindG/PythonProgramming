def allList(list1):
    for i in list1:
        if not i:
            return False
    return True
# If all values are true, it will return true.
# If at least one value is false, it will return false...
list1 = [True,False,True,False,True]

print(allList(list1)) #At least one value is false

list2 = [1,2,3,4,5] # All numbers are accepted true except that zero 0

print(allList(list2)) # All values are true

def anyValue(list2):
    for i in list2:
        if i:
            return True
    return False
# If one value is true, it will return true
# All values are false it will return false

list4 = [True,False,True,False,True]
print(anyValue(list4))

list5 = [0,0,0,0,0,0,0] # All values are false
print(anyValue(list5))

# all() Function
# all() function returns true if all values are true
# if at least one value is false it will return false

list6 = [True,False,True,False,True]
print(all(list6))

list7 = [1,2,3,4,5]
print(all(list7))

# any() Function
# any() function returns false if all values are false
# If at least one value is true it will return true

list8 = [True,False,True,False,True]
print(any(list8))

list9 = [0,0,0,0,0,0,0]
print(any(list9))