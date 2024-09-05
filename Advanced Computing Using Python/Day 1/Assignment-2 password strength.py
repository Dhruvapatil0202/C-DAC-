candidate_password = input("Enter Your Password: ")

lengthPw = len(candidate_password)

upperCase = 0
lowerCase = 0
specialChar = 0
numeric = 0

special_characters = "!@#$%&*(),.?/<>{}|\""

for character in candidate_password:
    if character.isupper():
        upperCase = 1
    if character.islower():
        lowerCase = 1
    if character in special_characters:
        specialChar = 1
    if character.isdigit():
        numeric = 1

score = upperCase + lowerCase + specialChar + numeric
if lengthPw >= 8: score += 1

if score <= 2: print("password is Weak")
elif score <= 4: print("password is Moderate")
elif score == 5: print("password is Strong")
