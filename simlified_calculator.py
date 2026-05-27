print("Simplified Calculator")

while True:

# Take 1st input from user
    num1 = float(input("Enter first number: "))

#Choose operation
    operation = input("Enter operation (+, -, *, /, **, %, v/): ")

# Take 2nd input from user
    num2 = float(input("Enter second number: "))

# Perform calculation
    if operation == "+":             # addition
        result = num1 + num2
    elif operation == "-":           # subtraction
        result = num1 - num2
    elif operation == "*":           # multiplication
        result = num1 * num2
    elif operation == "/":           # division
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    elif operation == "**":          # square
        result = num1 ** num2
    elif operation == "%":           # percentage
        result = (num2 / 100) * num1
    elif operation == "v/":          # "v/" -> root symbol (nth root)
        result = num2 ** (1 / num1)
    else:
        result = "Invalid operation"

    print("Result =", result)

    result = input("Do you want to continue? (y/n): ")

    if result == "n":
        break




