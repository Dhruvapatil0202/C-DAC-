
# words = input("Enter any text here: ").split(" ")
#
# unique_words = set(words)
#
# alpha_order = sorted(unique_words)
#
# print(alpha_order)

#______________________________________________________________

# txt = input("Enter input here: ").lower().split(" ")
# txt = "".join(txt)
#
# txt = sorted(set(txt))
# print(txt)
#
# # [a, b, c] "x"
# # axbxc

# quick brown fox jumps over the lazy dog
# __________________________________________________________________


print("".join(sorted(set("".join(input("Enter input here: ").lower().split(" "))))))

# s1, s2, s3 = set(), set(), set()
# ns = s1.intersection(s2.intersection(s3))