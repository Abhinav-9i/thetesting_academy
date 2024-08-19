# ✅ Literals

# variable_name = variable_value
# Python is dynamic types langugae -> literals value are ditermine the data type.
age = 65  # int

# decimal system ->  base  -> 10
age = 89  # 9

# binary - base system ->  2
binary_number = 0b1010  # 10

# Octal  -> base 8
o = 0o130  # - 88

# Hex  -> base 16
d = 0x12c

pi = 3.14  # float

is_pramod_married = False  # bool

# String , str
name = "Pramod"

# complex
complex_number = 1 + 7j

# list
my_list = ["pramod", "amit", "lucky"]

# tuple
my_tuple = ("bread", "apple", "milk")


#####
# Escape Sequence
print("Hello World")
print("Hello\nWorld") # \n -> newline
print("Hello\tWorld") # \t -> tabline
print("Hello\bWorld") # \b -> backspace

# dir = 'C:\pramod\n.txt'
# dir = "C:\pramod\n.txt"
# Where this r concept will be used?
# Automation API, Web Automation, file_path = r concept
dir = r"C:\pramod\n.txt"
dir2 = r'C:\pramod\n.txt'
print(dir)
print(dir2)
# Escape Seq. - Single
name = 'pramod\'utta'
name2 = "Pramod'utta"
print(name)
print(name2)


#####################
# Operators


age = 65
name = "pramod"
print(2+3)
print(2-3)
print(2*3)
print(2/3)


####################

# Operators

age = +65
print(age)
# Assignment  -> = which is used to store the right value to the light value ref.


# - - unary operator -
how_many_lambo_pramod = -1
print(how_many_lambo_pramod)


# Arthematic
# +, - , * , /
print(2+2)
print(2-2)
print(2/2)
print(2*2)



###############################

# x//y
# x%y
# x**y
# ==

print(5 // 2)  # ? Quotient
print(5 % 2)  # ? Remainder

# 2 | 5 | 2 - Quotient
#   | 4 |
# --------
#     1 - Remainder

print(13 // 2)
print(13 % 2)

# // and /
# / -> div
# // -> Quotient

print(2 ** 2)  # ** - power
print(2 ** 3)  # ** - power
print(2 ** 4)  # ** - power

#  ==  Compare Operator ( True or False

print(2 == 2)
print(2 == 3)





####################################
# Operators

# Not operator
is_pramod_married = True
print(not is_pramod_married) #! - java
print(is_pramod_married)

# is - this operator Java

# Logical Operator -> bool ->
# > , <  >= <=
x = 10
y = 20
print(x > y) # False
print(x < y) # True

a = 10
b = 10
print(a >= b) # 10 > 10 or 10 = 10
print(a == b)  # 10 = 10

# OR or And GATE
f = False
t = True
print(f or t)
print(f and t)



############################

x = 10
y = 20

# ! -> not -> int
# not -> bool
a = True
print(not a)
result = (x != y)  # 10 not equal 20 -> True
print(result)




#############################
# Ternary Operator

# if condition then do this
#     else do that

# if my_age > 13 then i can watch reels
#     else i can't watch'

# print("I will go GOA" if int(input("Enter your age")) > 18 else "Can't go, Stay Home ")

user_Age = int(input("Enter your age"))

if user_Age > 18:
    print("I will go GOA")
else:
    print("Can't go, Stay Home ")


###############################


















