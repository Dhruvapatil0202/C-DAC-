
# Using Space seperator
# name, age, address = tuple(input("Enter your info: ").split(" "))
# print(f"Name: {name} \nAge: {int(age)} \nAddress: {address}")

# ---------------------------------------------------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")
address = tuple(input("Enter your address: ").split(","))

details = (name, age, address)

name1, age1, address1 = details
city, state = address1

print(f"Name: {name1}, Age: {age1}, City: {city}, State: {state}")

