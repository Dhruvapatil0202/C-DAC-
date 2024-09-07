
def my_decorator(func):

    def wrapper():
        print('Before function')
        func()
        print('After function')

    print("Control in decorator function")
    wrapper()
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# say_hello = my_decorator(say_hello)