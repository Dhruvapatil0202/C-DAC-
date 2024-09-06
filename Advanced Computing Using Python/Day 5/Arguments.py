# special arguments

# def func1(*args):
#     return args[0] ** args[1]
#     pass
#
# print(func1(4, 3))
#
# def func2(param3 = 0, **kwargs):
#     return (kwargs["param1"] ** kwargs['param2']) + param3
#
# print(func2(param1 = 3, param2 = 4, param3 = 3))


def func3( *args, par1 = 2, par2= 3, **kwargs):
    print(par1 + par2)
    print(args)
    print(kwargs)
    pass

func3(4, 2, 3, 3, 9, par1 = 7, par2 = 9, temp = 7, j = 99)