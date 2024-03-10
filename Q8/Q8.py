import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
operation = random.choice(["+", "-"])

if operation == "+":
    correct_answer = number1 + number2
else:
    correct_answer = number1 - number2

while True:
    try:
        user_answer = int(input(f"What is {number1} {operation} {number2}? "))
        if user_answer == correct_answer:
            print("Congratulations! You've got the correct answer.")
            break
        else:
            print("Wrong answer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

