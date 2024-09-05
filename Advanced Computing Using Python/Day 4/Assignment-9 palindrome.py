

# string_inp = input("Enter the string here: ").strip()
#
#
# if string_inp == string_inp[::-1]:
#     print(f"{string_inp} is a palindrome string.")
# else:
#     print(f"{string_inp} is not a palindrome string. ")

#--------------------------------------------------------------------------------------

string = input("Enter any string: ").lower().strip()

newString = string[::-1]

if string == newString:
    print("Palindrome")
else:
    print("Not a Palindrome")