### formated
a=22/7
formated_nbr=f"{a:.5}"
print(a)
print(formated_nbr)


#Format string
num=90
print("My uncles age is "f"{num}")

table=9
print(f"{table}*1={table*1}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")

####Task 1:
table1=int(input("Enter value for which you want to see table: "))
print(f" Table of : {table1}" )
print(f"{table1}*1={table1*1}")
print(f"{table1}*2={table1*2}")
print(f"{table1}*3={table1*3}")
print(f"{table1}*4={table1*4}")
print(f"{table1}*5={table1*5}")

table3=float(input("Enter value for which you want to see table(float number): "))
print(f" table of : {table3}" )
print(f"{table3}*1={table3*1}")
print(f"{table3}*2={table3*2}")
print(f"{table3}*3={table3*3}")
print(f"{table3}*4={table3*4}")
print(f"{table3}*5={table3*5}")


# Task 2
a=int(input('Enter value of a: '))
b=int(input('Enter value of b: '))

print(f"sum of a and b is : {a+b}")
print(f"Subtraction  of a and b is : {a-b}")
print(f"Multiplication of a and b is : {a*b}")
print(f"Div of a and b is : {a/b}")
print(f"Power of a and b is : {pow(a,b)}")

