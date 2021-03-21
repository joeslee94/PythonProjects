#lambda arguments: expression usually used when a method is used once or is it used as a method that is used with a different argument
from functools import *
# #Lamda with simple functions
# addTenLambda = lambda num: num + 10
# #instead of making a method
# print(addTenLambda(5))
#
# multLambda = lambda num1, num2: num1*num2
# print(multLambda(4, 7))

# #Lambda with sort
# listOne = [(1, 2),
#            (4, 5),
#            (6, 7),
#            (8, 9),
#            (0, 5),
#            (5, 10)]
#
# listOneSorted = sorted(listOne, key = lambda num:num[0] ) #sort by first element
# listTwoSorted = sorted(listOne, key = lambda num:num[1] ) #sort by second element
# listThreeSum = sorted(listOne, key = lambda num:num[0] + num[1]) #sort by sum of the tuple
# print(listOne)
# print(listOneSorted)
# print(listTwoSorted)
# print(listThreeSum)

# #Lambda with map
# listOne = [1, 2, 3, 4, 5, 6]
# listTwo = map(lambda numInListOne: numInListOne * 2, listOne)
# print(list(listTwo))
#
# listThree = [num*2 for num in listOne] #list comprehension
# print(listThree)

## filter function and returns all elements that returns true.
# listOne = [1, 2, 3, 4, 5, 6]
# listTwo = filter(lambda numInListOne: numInListOne % 2 == 0, listOne)
# print(list(listTwo))
#
# listThree = [num % 2 == 0 for num in listOne] #returns true false
# listFour = [num for num in listOne if num % 2 == 0] #returns true false
# print(listThree)
# print(listFour)

## reduce function and sequence
listOne = [1, 2, 3, 4, 5, 6]
reduceOne = reduce(lambda num, num1: num*num1, listOne) #multiplies all the elements within the list
print(reduceOne)
