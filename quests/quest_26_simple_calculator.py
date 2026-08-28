#!/usr/bin/python3

def calculate():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    operation = input("Enter your operation:\n+\n-\n*\n/\nOperation: ")

    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2

    else:
        return ("Invalid input:\n"
                "1. Check if your first number is a number.\n"
                "2. Check if your second number is a number.\n"
                "3. Enter a valid operation (+, -, *, /).")
    
print(calculate())
