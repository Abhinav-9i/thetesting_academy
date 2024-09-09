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

if score >= 90 and score <= 100:  # Simplified Chaining Format -> 90 <= score <= 100
    print("You grade is ", "A")
elif score >= 80 and score <= 89:
    print("You grade is ", "B")
elif score >= 70 and score <= 79:
    print("You grade is ", "C")
elif score >= 60 and score <= 69:
    print("You grade is ", "D")
elif score >= 100:
    print("You are  Superman!!")
else:
    print("You grade is ", "F")


###########This was my running class practice
score=int(input("Enter score of student : \n"))
grade='F'

if score>=90 and score<=100:
    grade='A'
    print("your score is ",grade)
elif score>=80 and score<90:
    grade='B'
    print(f"your score hase {grade}")
elif score>=70 and score<80:
    grade='C'
    print(f"your score hase {grade}")
elif score>=60 and score<70:
    grade='D'
    print(f"your score hase {grade}")
else:
    print(f"your grade is ",grade)