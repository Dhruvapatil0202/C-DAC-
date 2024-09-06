"""Demonstration of Exception Handling in python"""

def func1(inp):
    """
    Function which raises Error if input is not the Integer
    :param inp: inp -> int
    :return: None
    """
    if type(inp) != int:
        raise(ValueError("Not an int"))
    else: print(inp)

def from_list(num_list, index):
    """
    function that returns the specific element from list
    :param num_list: list
    :param index: int
    :return: None
    """
    try:
        temp_var = num_list[index]
    except TypeError:
        raise TypeError(f"Int is expected to be int, got {type(index)} instead")
    except IndexError:
        raise IndexError(f"Index out of range")
    else:
        print(temp_var)
    finally:
        print("Code got executed successfully")

def div(num, divisor):
    """
    Prints the division of two inputted parameters
    :param num: int,
    :param divisor: int,
    :return: None
    """
    try:
        division = num / divisor
    except ZeroDivisionError:
        raise ZeroDivisionError("Got 0 as a divisor")
    else:
        print(division)
    finally:
        print("End of code")

# func1('3')
# from_list([1, 2, 3, 4, 5], '4')
# div(5, 0)

print(__doc__)
print(func1.__doc__)

#--------------------------------------------------------------------------------------
#
# def get_integer_input(number):
#
#     try:
#         number /= 1
#     except