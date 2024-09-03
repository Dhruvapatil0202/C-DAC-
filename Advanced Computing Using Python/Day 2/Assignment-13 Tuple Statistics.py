
member_tuple = tuple(map(int, input("Enter space separated numbers: ").split(" ")))
print(f"Entered elements: {member_tuple}")
print(f"Sum of all elements: {sum(member_tuple)}")
print(f"Avg of all elements: {sum(member_tuple) / len(member_tuple)}")
print(f"Maximum of all elements: {max(member_tuple)}")
print(f"Minimum of all elements: {min(member_tuple)}")
print(f"Number of elements in tuple: {len(member_tuple)}")

