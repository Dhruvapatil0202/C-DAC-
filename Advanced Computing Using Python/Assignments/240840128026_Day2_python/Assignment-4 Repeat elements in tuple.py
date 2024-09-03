
import sys
elements = tuple(input("Enter elements: ").strip().split(" "))

select_element_to_repeat = input(f"Enter element to repeat from {elements}: ").strip()
if select_element_to_repeat not in elements:
    print("Element does not exist in given set of elements.")
    # for i in elements:
    #     print(f"{i} {i == select_element_to_repeat}")
    sys.exit()

num = int(input("Enter number of times the element to be repeated: "))

temp = []
for i in elements:
    if i == select_element_to_repeat:
        for _ in range(num): temp.append(i)
    else:
        temp.append(i)

temp = tuple(temp)

print(f"Original tuple: {elements}")
print(f"Modified tuple: {temp}")


