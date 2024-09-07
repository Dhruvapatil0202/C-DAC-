import re

strs = ['Apple pie is delicious.' ,
      'Under the bed, there is a cat!' ,
      'Notes from the meeting!' ,
      '1234a5678b9aaa' ,
      'do not forget to check the details!']

# expression = r'^[aeiouAEIOU].*\w~[aeiou]$'
# exp = r'^[aeiouAEIOU].*[\w]?$'
#
# True_exp = r"\b[aeiouAEIOU]\w*\w~[aeiouAEIOU]\b"
# for str in strs:
#     out = re.match(exp, str.replace('.', '').strip())
#     print(out)


# exp_2 = r'[\d]+[^\d]'
# for str in strs:
#     out = re.findall(exp_2, str)
#     print(out)

# exp_3 = r'^Note.+!$'
# for str in strs:
#     out = re.findall(exp_3, str)
#     print(out)

#-----------------


for word in strs:
    if re.findall(r'^Note.*!$',word):
        print(word)