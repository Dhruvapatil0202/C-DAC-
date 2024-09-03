
tup = tuple(map(int,input("Enter list of numbers: ").split(" ")))

threshold = int(input("Enter the threshold: "))

tup = tuple(sorted(tup))

filtered_elements = tuple(i for i in tup if i > threshold)

print(f"Sorted elements: {tup}")
print(f"Filtered elements: {filtered_elements}")