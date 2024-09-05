countries_and_capitals = {
    "India": "New Delhi",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
    "South Africa": "Pretoria",
    "United Kingdom": "London",
    "United States": "Washington, D.C."
}

score = 0
attempts = 0
for country in countries_and_capitals:
    attempts += 1
    resp = input(f"What is capital of {country}: ")

    if resp.lower() == countries_and_capitals[country].lower():
        print("Correct Answer!!!")
        score += 1
    else:
        print(f"Incorrect Answer, correct answer is {countries_and_capitals[country]}")

    resp = input("Press X to exit. ")
    if resp.lower() == "x": break

print(f"You scored {score} points in {attempts} attempts.")
# _____________________________________________________________________________________


# score = 0
# attempted = 0
#
# print("Quiz")
# for country in countries_and_capitals:
#     print(f"What is the capital of {country}?")
#
#     ans = input(f"Enter you answer: ").lower()
#     attempted += 1
#
#     if ans == countries_and_capitals[country].lower():
#         score += 1
#         print(f"You are Correct! The capital of {country} is {countries_and_capitals[country]}")
#         print(f"Your current score is {score}")
#
#         choice = input(f"Do you want to continue or quit(Y/N): ").capitalize()
#
#         if choice == 'Y':
#             continue
#         else:
#             print(f"Your final score is {score} and you took {attempted} attempts to get that score")
#             break
#
#     else:
#         print(f"Your answer is Incorrect! Correct answer is {countries_and_capitals[country]}")
#         choice = input(f"Do you want to continue or quit(Y/N): ").capitalize()
#
#         if choice == 'Y':
#             continue
#         else:
#             print(f"Your final score is {score} and you took {attempted} attempts to get that score")
#             break


