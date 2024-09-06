

# temp = [1, 2, 3, 4, 5, 1, 2, 3]
# print({i : i ** 2 if i % 2 == 1 else i ** 3 for i in temp if i < 5 })
# print({i : temp.count(i)for i in set(temp)})

# print([i for i in range(2, 99) if all(i % div > 0 for div in range(2, int(i ** 0.5) + 1))])

def square(num): return num * num