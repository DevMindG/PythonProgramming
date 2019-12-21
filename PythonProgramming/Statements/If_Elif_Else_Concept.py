
"""
position = int(input("Select position: "))  # 3 positions.

if position == 1:
    print("1. position is selected.")
elif position == 2:
    print("2. position is selected.")
elif position == 3:
    print("3. position is selected.")
else:
    print("Invalid position!")

"""
"""
score = float(input("Enter your score: "))

if score >= 90:
    print("AA")
elif score >= 85:
    print("BA")
elif score >= 90:
    print("BA")
elif score >= 80:
    print("BB")
elif score >= 75:
    print("CB")
elif score >= 70:
    print("CC")
elif score >= 65:
    print("DC")
elif score >= 60:
    print("DD")
else:
    print("Failed")

"""

# if you change elif to if, in python all conditions are worked and if they are true, python works
# true condition

score = float(input("Enter your score: "))

if score >= 90:
    print("AA")
elif score >= 85:
    print("BA")
if score >= 90:
    print("BA")
if score >= 80:
    print("BB")
if score >= 75:
    print("CB")
if score >= 70:
    print("CC")
if score >= 65:
    print("DC")
if score >= 60:
    print("DD")
else:
    print("Failed")
