# two different decorators function/class
# function takes another function without explicitly modifying it
# decorators adds functionality
import functools

# def startEndDecorator(func):
#
#     @functools.wraps(func) #fixes the identity of the function
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# @startEndDecorator
# def printName():
#     print('Joe')

# printName()
# printName = startEndDecorator(printName) is the same as putting @startEndDecorator above func
# printName()

# @startEndDecorator
# def addFive(x):
#     return x + 5
#
# print(help(addFive))
# print(addFive.__name__)

# def repeat(iteration):
#     def decoratorRepeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(iteration):
#                 greeting = func(*args, **kwargs)
#             return greeting
#         return wrapper
#     return decoratorRepeat
#
# @repeat(iteration = 3)

# def startEndDecorator(func):
#
#     @functools.wraps(func) #fixes the identity of the function
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper
#
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         argsRepr = [repr(a) for a in args]
#         kwargsRepr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(argsRepr + kwargsRepr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper
#
# @debug
# @startEndDecorator
# def greet(name):
#     greeting = f"Hello {name}"
#     print(greeting)
#     return greeting

# greet('Joe')

class countCalls:
    def __init__(self, func):
        self.func = func
        self.numCalls = 0

    def __call__(self, *args, **kwargs):
        self.numCalls += 1
        print(f"This has executed {self.numCalls} times")
        return self.func(*args, **kwargs)

@countCalls
def greeting():
    print("Hello")

greeting()
greeting()
greeting()
greeting()