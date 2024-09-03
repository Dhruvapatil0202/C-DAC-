

while True:

    num1 = int(input("Enter number number: "))
    num2 = int(input("Enter second number: "))

    operation = "x"
    operations = "-+*/"
    while operation not in operations:
        operation = input("Enter operation (+, -, *, /): ")
        if operation not in operations: print("Invalid operator")

    match operation:
        case "+": print(f"{num1} + {num2} = {num1 + num2}")
        case "-": print(f"{num1} - {num2} = {num1 - num2}")
        case "*": print(f"{num1} X {num2} = {num1 * num2}")
        case "/": print(f"{num1} / {num2} = {num1 / num2}")

    quit_resp = input("Do you want to continue? Y/N: ")
    if quit_resp not in "Yy": 
        break



