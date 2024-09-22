
def slice_string(inp_string):
    first_five = inp_string[:5]
    last_five = inp_string[-5:]
    ln = len(inp_string)
    if ln % 2 == 0:
        middle = inp_string[(ln//2) - 1: (ln//2) + 1]
    else:
        middle = inp_string[(ln//2) - 1: (ln//2) + 2]
    every_second = inp_string[::2]
    return (first_five, last_five, middle, every_second)


# abcdefg  7

print(slice_string("abcdef"))