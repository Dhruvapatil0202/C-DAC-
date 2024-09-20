
list1 = [100,200,300,400,500]
reversed_list = list1[::-1]
print(reversed_list)


list2 = list(map(int,input("Enter the list of integers seperated by , :").split(",")))

print(f"Largest number in the list is {max(list2)}")
print(f"Smallest number in the list is {min(list2)}")