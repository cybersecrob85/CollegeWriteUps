#Robert Potter, 11/13/2025, Milestone 3

#Greet user
print(f"Welcome to the Simple Calculator Program.")

#Ask user for two numbers and Enter the operation they want
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation you want to perform (+, -, *, /): ")

#Define a functions for each operation
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b


#Perform the selected operation
if operation == "+":
    result = add(num1, num2)    
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)

#Display the result
print(f"The result of the {operation} of {num1} and {num2} is: {result}")

#Thanks for using the calculator
print(f"Thank you for using the Basic Calculator Program!")