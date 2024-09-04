
def calc(num1, num2, operation):
    match operation:
        case "+": output = num1 + num2
        case "-": output = num1 - num2
        case "*": output = num1 * num2
        case "/": output = num1 / num2
    return output

num1, num2 = int(input("Enter number one: ")), int(input("Enter number two: "))

operation = "x"
while operation not in "-+*/":
    operation = input("Enter operation (+, -, *, /): ")
    if operation not in "-+*/":
        print("Entered operation is Invalid.")

output = calc(num1, num2, operation)

print(f"{num1} {operation} {num2} = {output}\n")

while True:

    quit_inp = "x"
    while quit_inp not in "yn":
        quit_inp = input("Do you want to process further on previous result? Y/N: ").lower()
        if quit_inp not in "yn": print("Invalid input")

    if quit_inp != "y": break
    else:
        num2 = int(input("Enter second number: "))

        operation = "x"
        while operation not in "-+*/":
            operation = input("Enter operation (+, -, *, /): ")
            if operation not in "-+*/":
                print("Entered operation is Invalid.")
        
        new_out = calc(output, num2, operation)

        print(f"{output} {operation} {num2} = {new_out}\n")
        output = new_out




    
    