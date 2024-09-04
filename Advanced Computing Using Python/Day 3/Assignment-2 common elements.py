#
# tup1 = tuple(input("Enter the elements inside the first tuple: ").split(","))
# tup2 = tuple(input("Enter the elements inside the second tuple: ").split(","))
#
# set1 = set(tup1)
# set2 = set(tup2)
#
# newTuple = tuple(set1.intersection(set2))
# print(f"New Tuple: {newTuple}")


# _____________________________________________________________________________

tuple1 = input("Enter first set of elements: ").split(" ")
tuple2 = input("Enter second set of elements: ").split(" ")
# s1, s2 = set(tuple1), set(tuple2)
# s3 = s1.intersection(s2)
# print(s3)
print(tuple(set(tuple1).intersection(set(tuple2))))