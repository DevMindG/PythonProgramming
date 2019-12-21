"""
try:


  We can define here our code. If code throws an exception,
  system will go related except block

except 1:

except 2:

"""

try:
    a = int("asaj12345ksjx")
    print("This block is try block")
except:
    print("Exception occurs...")
print("Blocks will be closed")


try:
    a = int("23")
    print("This block is try block")
except:
    print("Exception occurs...")
print("Blocks will be closed")

try:
    a = int("asaj12345ksjx")
    print("This block is try block")
except ValueError:
    print("Exception occurs...")
print("Blocks will be closed")

"""
try:
    a = int(input("Number1: "))
    b = int(input("Number2: "))
    print(a / b)
except ValueError:
    print("Please enter correct input")
except ZeroDivisionError:
    print("A number cannot be divided with zero")
print("Blocks are closed...")


"""
"""
try:
    a = int(input("Number1: "))
    b = int(input("Number2: "))
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Please enter correct input")
print("Blocks are closed...")


"""
"""
try:
    a = int(input("Number1: "))
    b = int(input("Number2: "))
    print(a / b)
except ValueError:
    print("Please enter correct input")
except ZeroDivisionError:
    print("A number cannot be divided with zero")
finally:
    print("Finally works in every circumstances")
print("Blocks are closed...")


"""

def reverseStr(s):
    if type(s) != str:
        raise ValueError("Enter a String value")
    else:
        return s[::-1]

print(reverseStr("Python"))

# print(reverseStr(12))

try:
    print(reverseStr(12))
except ValueError:
    print("It gave error")
