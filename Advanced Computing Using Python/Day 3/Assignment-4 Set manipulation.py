
# st_1 = {1, 2, 3, 4, 5, 6, 7}
# st_2 = {10, 0, 8, 2, 3, 11, 6}
# st_3 = {20, 23, 2, 3, 1, 10, 11}
#
# # Items common in all sets:
# print("\ncommon in all sets")
# print(sorted(st_1.intersection(st_2.intersection(st_3))))
#
# # Items present in st1 and st2 but not in st3
# print("\nin st1 and st2 but not in st3")
# print(sorted(st_1.intersection(st_2) - st_3))
#
# # Items present in st2 and st3 but not in st1
# print("\nin st2 and st3 but not in st1")
# print(sorted(st_2.intersection(st_3) - st_1))
#
# # Items present in st3 and st1 but not in st2
# print("\nin st3 and st1 but not in st2")
# print(sorted(st_3.intersection(st_1) - st_2))
#
# # items present in only in st1:
# print("\nonly in st1")
# print(sorted(st_1 - st_2.union(st_3)))
#
# # items present only in st2:
# print("\nonly in st2")
# print(sorted(st_2 - st_1.union(st_3)))
#
# # items present only in st3:
# print("\nonly in st3")
# print(sorted(st_3 - st_1.union(st_2)))
#
# # Items not common to any of the three sets:
# print("\npresent in any one or two sets")
# print(sorted(st_1.union(st_2.union(st_3)) - st_1.intersection(st_2.intersection(st_3))))

#_-----------------------------------------------------------------------------------------

set1 = {23,54,1,4,7,54,200,300}
set2 = {1,4,88,99,100,23,500}
set3 = {1,4,88,54,500,1000,200,300}

#Items common to all three sets(Intersection)
set1IntSet2 = set1.intersection(set2)
set1IntSet3 = set1.intersection(set3)
set2IntSet3 = set2.intersection(set3)
print(f"Intersection: {set1IntSet2.intersection(set1IntSet3.intersection(set2IntSet3))}")

# Items not common to any of the three sets (Symmetric Difference)
symDiff = set1.symmetric_difference(set2).symmetric_difference(set3)
print(f"Symmetric Difference: {symDiff}")

# Items unique to each set(Difference)
print(f"Difference: {symDiff-set1IntSet2.intersection(set1IntSet3.intersection(set2IntSet3))}")