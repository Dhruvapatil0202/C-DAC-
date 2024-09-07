# import logging
#
#
# def log_execution(log_file, log_level = logging.DEBUG):
#
#     logging.basicConfig(
#         filename= log_file,
#         level= log_level,
#         format= "%(asctime)s - %(levelname)s - %(message)s"
#     )
#
#     def decorator(func):
#
#         def wrapper(*args, **kwargs):
#             logging.log(log_level, f"Starting {func.__name__}")
#             result = func(*args, **kwargs)
#             logging.log(log_level, f"Ending {func.__name__}")
#             return result
#         return wrapper
#     return decorator
#
# @log_execution('basiclogger.log')
# def func_tion(string):
#     print(string)
#
# func_tion('Hello from func_tion')

#---------------------------------------------------------------------------------


import logging

def log_execution(fileName = "logDetails.log", log_level = logging.DEBUG):

    logging.basicConfig(
        filename=fileName,
        level= log_level,
        format= "%(asctime)s - %(levelname)s - %(message)s"
    )
    def decorator(func):

        def wrapper(*args, **kwargs):

            logging.log(level=log_level,msg=f"{func.__name__} has begun")
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                logging.log(msg=f"{func.__name__} has ({error}) error", level=logging.ERROR)
            else:
                logging.log(msg=f"{func.__name__} has ended", level=log_level)

            return result
        return wrapper
    return decorator

@log_execution(fileName = "logdetails2.log", log_level = logging.INFO)
def greet(string):
    print(f"{string} ^ 2 = {string ** 2}")

greet("2")