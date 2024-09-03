# print("Type 1")
# input_number = input("Input the required Number: ")
#
# count = 0
# for str_digit in input_number:
#     if str_digit.isdigit():
#         count += int(str_digit)
# print(f"The sum of digits from inputted numbers is: {count}")

# ________________________________________________________________

# print("Type 2")
# input_number = input("Input required Number: ")
#
# count = 0
# for str_digit in input_number:
#     if str_digit.isdigit():
#         count += ord(str_digit) - ord("0")
# print(f"The sum of digits from inputted numbers is: {count}")

#_________________________________________________________________

print("Type 3")
input_number = int(input("Input required Number: "))

count = 0
while input_number >= 10:
    count += input_number % 10
    input_number //= 10
count += input_number
print(f"The sum of digits from inputted numbers is: {count}")

# ________________________________________________________________

# num = input("Enter any positive integer")
#
# sum = 0
#
# for digit in num:
#
#     sum += int(digit)
#
# print(f"The sum of the digits of entered number is {sum}")


