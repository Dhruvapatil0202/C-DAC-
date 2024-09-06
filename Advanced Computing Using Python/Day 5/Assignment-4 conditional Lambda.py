

# print(list(map(lambda x: "positive" if x > 0 else("negative" if x < 0 else "zero") , [10, -4, 0, 7, -3, 4, -2, 3, 0])))

#-----------------------------------------------------------------------------------------------------------------------

numbers = [10,-5,0,7,-3,4,-2]

# updated_list = map(lambda number for number in numbers : "Positive" if (number>0) else "Negative" if (number<0) else "Zero", numbers)
updated_list = map(lambda number: "Positive" if number>0 else "Negative" if number<0 else "Zero", numbers)
print(list(updated_list))