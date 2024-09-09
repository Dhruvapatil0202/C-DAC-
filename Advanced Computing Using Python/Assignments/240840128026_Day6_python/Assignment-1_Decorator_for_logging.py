import logging
import time
LOG_FILE = 'decoratorExampleLog.log'

def logger_decorator(filename):
    logging.basicConfig(
        filename = filename,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        level = logging.DEBUG,
    )

    def decorator(func):

        def wrapper(*args, **kwargs):
            out = None
            try:
                out = func(*args, **kwargs)
            except Exception as exc:
                logging.log(
                    level = logging.ERROR,
                    msg = f"Error ({exc}) occured in execution of {func.__name__}"
                )
                return None
            else: 
                pass

            return out
        
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

def execution_time_decorator(filename):
    logging.basicConfig(
        level= logging.DEBUG,
        filename= filename,
        format = "%(asctime)s - %(levelname)s - %(message)s"
    )

    def decorator(func):

        def wrapper(*args, **kwargs):
            start_time = time.time()
            out = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            logging.log(
                level = logging.DEBUG,
                msg = f"Execution time for {func.__name__} to get executed is {execution_time}"
            )

            return out
        
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

@execution_time_decorator(LOG_FILE)
@logger_decorator(LOG_FILE)
def func_exec(input):
    print(f"\nOutput from func_exec: \t{input} ^ 2 = {input ** 2}\n")

if __name__ == "__main__":
    
    # Input string to check the error log, int to check execution time log
    func_exec("3")

    


