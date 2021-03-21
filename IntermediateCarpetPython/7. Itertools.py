# itertools: product, permutation, combinations, accumulate, grouby, and infinite
from itertools import *
import operator

# #products
# a = [1, 2]
# b = [3, 4]
# productOne = product(a, b, repeat = 2) # number of times we want it to repeat
# print(list(productOne))  # must make it a list to view

# #permutation
# a = [1, 2, 3]
# perm = permutations(a) #permutat for the length of the list
# perm2 = permutations(a, 2) #permutate only for a list that is 2 elements deep
# print(list(perm)) #permutation for only 2 elements
# print(list(perm2)) #all permutations

##combination make combinations of all elements and return a list for length specified
# a = [1, 2, 3, 4, 5]
# comb = combinations(a, 3)
# comb2 = combinations(a, 2)
# comb3 = combinations(a, 1)
# comb4 = combinations(a, 4)
# print(list(comb))
# print(list(comb2))
# print(list(comb3))
# print(list(comb4))
#
# combWR = combinations_with_replacement(a, 2) # able to print doubles of the list above
# print(list(combWR))

##accumulate adds the next element with the previous element
a = [1, 2, 7, 3, 4]
accumOne = accumulate(a)
accumTwo = accumulate(a, func=operator.mul) # multiples instead of adding
accumThree = accumulate(a, func=max) # returns max of the two elements
print(a)
print(list(accumOne))
print(list(accumTwo))
print(list(accumThree))

##groupby makes an iterator that returns keys and iterables
# def lessThan3(num):
#     return num < 3
# groupOne = groupby(a, key=lessThan3)

groupOne = groupby(a, key=lambda num: num < 3)

for key, value in groupOne:
    print(key, list(value))

## excellent itertool that allows the list to be separated according to what elements follow the methods rule

peopleNameAge = [{'name': 'Tim', 'age': 25},
                 {'name': 'Dan', 'age': 26},
                 {'name': 'Lisa', 'age': 27},
                 {'name': 'Joe', 'age': 28}]

groupTwo = groupby(peopleNameAge, key = lambda age: age['age'])
for key, age in groupTwo:
    print(key, list(age))

# #infinite iterators count, cycle, repeat
# for i in count(10):
#     print(i)
#     if i == 15:
#         break
#
# for i in cycle(a):
#     print(i)

for i in repeat(a, 4): #number is how many times i want the repeat to complete
    print(i)