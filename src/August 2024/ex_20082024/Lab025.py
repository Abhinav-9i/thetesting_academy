# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 ->  O/p -> str -> A or B....

score = int(input("Enter your score\n"))
# score >=90 and scroe <=100 -> "A"
# score >=80 and scroe <=89 -> "B"

if 90 <= score <= 100:  # Simplified Chaining Format -> 90 <= score <= 100
    print("You grade is ", "A")
elif 80 <= score <= 89:
    print("You grade is ", "B")
elif 70 <= score <= 79:
    print("You grade is ", "C")
elif 60 <= score <= 69:
    print("You grade is ", "D")
elif score >= 100:
    print("You are  Superman!!")
else:
    print("You grade is ", "F")