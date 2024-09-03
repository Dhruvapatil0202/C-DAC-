from random import randint

number = randint(1, 101)
attempts = 0
while attempts < 10:
    attempts += 1
    guess = int(input("Guess the number: "))

    if(guess == number):
        print("Your guess is correct!")
        break
    elif guess < number:
        print("Your guess is less than the actual number")

    elif guess > number:
        print("Your guess is greater than the actual number")

if attempts == 10: print("You Failed to guess the number")

