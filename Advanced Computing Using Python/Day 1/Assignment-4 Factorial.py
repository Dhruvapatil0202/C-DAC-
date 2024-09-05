

# number = int(input("Enter the number to calculate Factorial: "))
# if number == 0: factorial = 1
# else:
#     temp = number
#     factorial = 1
#     while temp > 1:
#         factorial *= temp
#         temp -= 1
# print(f"The factorial of {number} is {factorial}")


number = int(input("Enter the number to calculate the factorial: "))

fact = 1


if(number == 0):
    print(f"Factorial of {number} is 1")
else:
    for i in range (1,number+1):
        fact *= i

    print(f"Factorial of {number} is {fact}")
