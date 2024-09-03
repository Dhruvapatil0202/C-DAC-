
item_list = input("Enter your list separated by spaces: ").split(" ")
# item_list = []

# for item in temp_list:
#     if item == " " or item == ",":
#         continue
#     else:
#         item_list.append(item)

original_list = item_list[:]
positions = int(input("Enter the number of positions to rotate the list: "))
positions %= len(item_list)

for i in range(0, positions):
    temp = item_list.pop(-1)
    item_list.insert(0, temp)

print(original_list)
print(item_list)

