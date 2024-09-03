import math


# prime_numbers = []
# limit = int(input("Enter the number: "))
#
# curr = 2
# for candidate in range(2, limit+1):
#     flg = True
#     for div in range(2, int(math.sqrt(candidate)) + 1):
#         if candidate % div == 0:
#             flg = False
#             break
#         else:
#             continue
#     if flg: prime_numbers.append(candidate)
# print(prime_numbers)

# ____________________________________________________________________

num = int(input("Enter a positive number: "))

def primeOrNot(item):
    for i in range(2, int(math.sqrt(item))+1):
        if(item % i == 0):
            return False

    return True

list_prime = []

for i in range(2, num+1):
    if primeOrNot(i):
        list_prime.append(i)

print(list_prime)


