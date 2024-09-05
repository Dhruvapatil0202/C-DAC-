

# text_inp = "word word1 word2 word3 word4 word5"
#
# print(text_inp.find('word3'))
#
# temp = text_inp
# st_ind = 0
# disp_list = []
# while True:
#     if st_ind >= len(temp): break
#     inst = temp.find('word', st_ind)
#     if inst == -1: break
#     disp_list.append(inst)
#     st_ind = inst + 1
# print(disp_list)
#
# print(text_inp.replace('word', 'wrod', 4))
#
# print(text_inp.replace('word', 'wwe'))
# print(text_inp)

# _______________________________________________________________

string = "abcdpqrshijabchijkabc"

substring = "abc"
count = 0
index = 0
while True:
    index = string[index:].find(substring)
    if index == -1:
        print("No occurence of a substring in the given string")
        break
    print(index)


