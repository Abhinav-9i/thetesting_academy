# Conditions and Loops

# Write a program to take a user age and let him know if he can go the club.
# 21

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.


# 2. Rough loigc
# age  > 21 -> print can go
# age < 21 -> print can't go


# 3. write the logic
age = input("Enter you age\n")
age = int(age)

if age >= 21:
    print(f"Can go Club -> {age}")
else:
    print(f"Can't go with this age -> {age}")

age1 =input("Please enter your age")
age1=int(age1)


if age1>=21:
    print('You are allowed')
else:
    print(f"you can not go with {age1}")