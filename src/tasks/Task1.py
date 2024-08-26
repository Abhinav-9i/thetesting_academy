"""Task #1
Home Can you create a Program I will give you number(userinput and print table)

User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10"""
####Done


# Task #1: Multiplication Table

# Get user input
num = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table
print(f"Multiplication Table for {num}:\n")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")






