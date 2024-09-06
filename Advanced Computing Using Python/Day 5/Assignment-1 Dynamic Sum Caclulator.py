

# def sum_numbers(*args):
#     return sum(i for i in args if i >= 0)
#
# print(sum_numbers(1, 3, 4, -7, 3 ,-4 , -5))

#-----------------------------------------------------

def sum_numbers(*args):

    sum = 0
    for num in args:
        if num > 0:
            sum += num

    return sum

print(sum_numbers(1,2,3,4,5,-34,-10))