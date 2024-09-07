
# Decorators are used to extend the functionality of the current function
# new code is added to either end of the code of the function
# Returns new function
# Add functionality to existing code in a clean an readable way


# decorators may or may not take arguments.
#
# def simple_logger(in_function):
#
#     def wrapper(*args, **kwargs):
#         print(f"starting {in_function.__name__}")
#         out = in_function(*args, **kwargs)
#         print(f"finished {in_function.__name__}")
#         return out
#
#     return wrapper
#
# @simple_logger
# def greet(name):
#     print(f"hello {name}")
#
# greet("Person")

# -----------------------------------------------------------------------------

    # def simple_logger(func):
    #     def wrapper(*args, **kwargs):
    #         print(f"Starting {func.__name__}...")
    #         result = func(*args,**kwargs)
    #         print(f"Finished {func.__name__}")
    #         return result
    #     return wrapper
    #
    # @simple_logger
    # def greet(name):
    #     print(f"hello {name}")
    #
    # print(greet('Alice'))

#__________________________________________________________________________________________

# decorators using arguments
import logging
def log_to_file(log_file, log_level = logging.INFO):

    logging.basicConfig(
        filename = log_file,
        level = log_level,
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )

    def decorator(function):

        def wrapper(*args, **kwargs):
            logging.log(log_level, f"starting {function.__name__}")
            result = function(*args, **kwargs)
            logging.log(log_level, f"ending {function.__name__}")
            return result

        return wrapper

    return decorator
@log_to_file(log_file = 'custom_log.log' )
def greet(name):
    print(f"hello {name}")

print(greet('Alice'))


