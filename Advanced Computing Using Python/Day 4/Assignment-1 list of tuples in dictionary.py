
# input_str = input("Enter elements of tuples separated by \',\': ").split(" ")
# tuple_list = [tuple(str.split(',')) for str in input_str]
# cand_dict = {i : j for i, j in tuple_list}
# print(cand_dict)


# print({i : j for i, j in [tuple(str.split(',')) for str in input("Enter elements of tuples separated by \',\': ").split(" ")]})


# ______________________________________________________________________________________________

tuple_list = [tuple(x.split(",")) for x in input("Enter the list of tuples containing key value pairs: ").split(" ")]

dict_tuple = {key:value for key,value in tuple_list}
print(dict_tuple)