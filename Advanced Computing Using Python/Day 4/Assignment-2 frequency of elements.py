# input = input("Enter string here: ")
# dictionary = {}
# for i in input:
#     if i in dictionary:
#         dictionary[i] += 1
#     else:
#         dictionary[i] = 1
# print(dictionary)

# _________________________________________________________________________

# list_text = input("Enter the list of elements: ").split(" ")
#
# dict_frequency = {}
#
# for element in list_text:
#     if element in  dict_frequency:
#         dict_frequency[element] += 1
#     else:
#         dict_frequency[element] = 1
#
#
# print(dict_frequency)

#___________________________________________________________

# import collections
# temp = dict(collections.Counter("snfoinweonfiowneoihnfowieg"))
# print(temp)

input = "ojfionweoinowinegionwioengnweng"
# dictionary = {}
# for i in input:
#     if i in dictionary:
#         dictionary[i] += 1
#     else:
#         dictionary[i] = 1
# print(dictionary)

temp = {i : input.count(i) for i in input}
print(temp)