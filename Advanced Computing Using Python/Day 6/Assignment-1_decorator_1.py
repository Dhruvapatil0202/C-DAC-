

# def func_name_printer(function):
#     def wrapper(*args, **kwargs):
#         print(f"{function.__name__} is being executed. ")
#         out = function(*args, **kwargs)
#         print(f"{function.__name__} is done executing. ")
#         return out
#     return wrapper
#
# @func_name_printer
# def greet(name):
#     print(f"Hello {name}")
#
# greet("Someone")

# ___________________________________________________________________

def test_decorator(temp):

    def decorator(func):

        def wrapper(*args):
            print(func.__name__)
            res = func(*args) + temp
            return res
        return wrapper
    return decorator

@test_decorator("morning")
def greeting(name):
    print(f"Good {name}")


greeting()