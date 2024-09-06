
import sys
#
# if __name__ == "__main__":
#
#     file1, file2 = 'ass2_file1', 'Report'
#     try:
#         with open(file1, 'r') as file:
#             string_li = file.readlines()
#         with open(file2, 'r') as file:
#             string_li2 = file.readlines()
#         all_text = set(string_li2 + string_li)
#     except:
#         print("Error occurred in reading files. ")
#         sys.exit()
#     text = "".join(all_text)
#     with open(file1, 'w') as file:
#         file.write(text)
#
#     print(string_li + string_li2)

#------------------------------------------------------------------------

fileName1, fileName2 = "ass2_file11","Report1"

with open(fileName1,'r') as file:
    file1 = file.readlines()

with open(fileName2,'r') as file:
    file2 = file.readlines()

file1 += file2

mergedata = set(file1)
print(mergedata)
mergedata = "".join(mergedata)
with open("merged_file",'w') as file:
    file.write(mergedata)





