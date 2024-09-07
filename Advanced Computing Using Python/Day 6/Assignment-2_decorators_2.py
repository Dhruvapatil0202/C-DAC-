import time

# def log_func_name(func):
#
#     def wrapper(*args, **kwargs):
#         print(f"{func.__name__}")
#         out = func(*args, **kwargs)
#         return out
#     return wrapper
#
# def log_exec_time(func):
#
#     def wrapper2(*args, **kwargs):
#         temp = time.time()
#         out = func(*args, **kwargs)
#         temp_after = time.time()
#         print(temp_after - temp)
#         return out
#     return wrapper2
#
# @log_exec_time
# @log_func_name
# def temp_func(secs):
#     time.sleep(secs)
#
# temp_func(3)

#-------------------------------------------------------------------------------

import time

def log_func_name(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)
        func(*args, **kwargs)
    return wrapper

def lof_execution_time(func):
    def wrapper(*args, **kwargs):
        time_before = time.time()
        func(*args,**kwargs)
        time_after = time.time()
        print(time_after-time_before)
    return wrapper


@lof_execution_time
@log_func_name
def execute_time(sec=3):
    time.sleep(sec)

execute_time(2)