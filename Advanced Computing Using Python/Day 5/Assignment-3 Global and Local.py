

# global_sum = 0
#
# def sum_func(sum_list):
#     global global_sum
#     global_sum = sum(sum_list)
#
# print(global_sum)
# sum_func([1, 2, 3, 4])
# print(global_sum)

#-------------------------------------------------------------------

sum1 = 0

def sum_numbers(*args):

    sum1 = 0
    for num in args:
        sum1 += num

    return sum1


def global_sum(num):
    global sum1
    sum1 = num

sum2 = sum_numbers(1,3,5)
print(f"Before updating global {sum1}")
global_sum(sum2)
print(f"After updating global {sum1}")



