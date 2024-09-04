#
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict)
# print({i : j for j, i in dict.items()})

#------------------------------------------------------------------------------

dict = {1:"w",3:"f",9:"3",2:"v"}

new_dict = {dict[key]:key for key in dict}
print(new_dict)