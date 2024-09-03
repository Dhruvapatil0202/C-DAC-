

num = int(input("Enter limit for Fibonacci Series: "))

one, two = 0, 1
print(f"{one} \n{two}")

for i in range(num - 2):
    new = one + two
    one, two = two, new
    print(two)

