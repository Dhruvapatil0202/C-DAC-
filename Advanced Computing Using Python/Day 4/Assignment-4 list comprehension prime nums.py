
# prime_numbers = [prime for prime in range(2,51) if prime]
#
# for num in range(2, 51):
#
#     for div in range(2, num):
#         if num % div == 0

# print([i for i in [num if sum([1 if num % div == 0 else 0 for div in range(2, num)]) == 0 else "" for num in range(2, 51)] if type(i) == int])


# print([num for num in range(2, 51) if sum([1 if num % div == 0 else 0 for div in range(2, num)]) == 0])

# ______________________________________________________________________________________________________________

# import math
#
# print([prime for prime in range(2,51) if [prime % x for x in range(2,int(math.sqrt(prime))+1)].count(0) == 0])

print(5 ** 0.2)