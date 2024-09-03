

tup = tuple(map(int, input("Enter the list of numbers: ").split(sep=",")))
print(tup)

print(f"First element in the tuple is : {tup[0]}")
print(f"Last element in the tuple is : {tup[-1]}")
print(f"Tuple excluding first and last element is : {tup[1:-1]}")
print(f"Slicing tuple with steps : {tup[1: len(tup) + 1: 2]}")
print(f"Reversed tuple: {tup[::-1]}")

