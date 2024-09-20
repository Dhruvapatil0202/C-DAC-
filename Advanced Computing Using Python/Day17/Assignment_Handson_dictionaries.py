
dict = {'Arham':'Blue', 'Lisa':'Yellow', 'Vinod':'Purple', 'Jenny': 'Pink', 'Bob': 'White'}

print(f"Total no. of students: {len(dict)}")

dict["Lisa"] = "Black"

del dict["Jenny"]

sorted_dict = {key:dict[key] for key in sorted(dict)}

print(dict)
print(sorted_dict)


