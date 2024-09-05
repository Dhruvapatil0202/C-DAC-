
while True:

    num1 = float(input("Input num1: "))
    num2 = float(input("input num2: "))

    operation = "x"
    while operation not in "+-/*":
        operation = input("Enter The operation(+, -, /, *): ")
        if operation not in "+-/*":
            print("Invalid Input")

    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        print(f"{num1} / {num2} = {num1 / num2}")

    response = input("Do you want to continue Y/N: ")
    if response == "N": break


