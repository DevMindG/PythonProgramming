
def reverseFunction(s):
    if type(s) != str:
        raise ValueError("Enter string value")
    else:
        return s[::-1]

print(reverseFunction("Python"))


# print(reverseFunction(12))

try:
    print(reverseFunction(12))
except ValueError:
    print("Function gives an error")

