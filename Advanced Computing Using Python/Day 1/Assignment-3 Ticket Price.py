age = int(input("Enter your age: "))

price = 0

if age < 5:
    price = 0
elif age >= 5 and age <= 12:
    price = 5
elif age >= 13 and age <= 60:
    price = 10
else:
    price = 7

print(f"Ticket Price: {price}")