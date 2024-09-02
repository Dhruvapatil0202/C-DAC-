
while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation = "x"
    while operation not in "+-*/":
        operation = input("Enter the operation (+, -, *, /): ")
        if operation not in "+-*/": print("Invalid operation")

    if operation == "+":
        print(f"{num1} {operation} {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} {operation} {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} {operation} {num2} = {num1 * num2}")
    elif operation == "/":
        print(f"{num1} {operation} {num2} = {num1 / num2}")

    response = input("Do you want to continue? press 'n' for NO: ")
    if response == "n":
        break

