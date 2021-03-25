# Errors and Exceptions
#import errors, formatting errors, value errors

##Handling errors

# #Manually coding exceptions
# num = -5
# if num < 0:
#     raise Exception("x cannot be negative")

# #Assert
# numTwo = -9
# assert(numTwo >= 0), "x is not positive."

## Try/Catch (EXCEPT)
# try:
#     a = 5 / 1
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everthing is fine')
# finally:
#     print('cleaning up....')

## My own exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def testValue(num):
    if num > 100:
        raise ValueTooHighError("Value is too high")
    if num < 5:
        raise ValueTooSmallError("Value is too small", num)

try:
    testValue(4)
except ValueTooHighError as e:
    print(e)
except ValueTooHighError as e:
    print(e.message, e.value)