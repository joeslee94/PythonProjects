# Sets unordered mutable NO DUPLICATES
setOne = {1, 2, 2, 3, 4, 5, 6}
# print(type(setOne))
#
# setTwo = set([1, 2, 3])
# setThree = set("Hello")
#
# print(setTwo)
# print(setThree)

## Empty set needs to be like the following
setFour = set()
setFour.add(1)
setFour.add(2)
setFour.add(3)
setFour.add(4)

# setFour.discard(3)
# setFour.clear()
# print(setFour.pop())
# print(setFour)

## Iterate through set
# for i in setFour:
#     print(i)

## Check to see if element is in set can use if statement
## Combines sets without duplication
setFive = {2, 4, 6, 8}
#setUnion = setOne.union(setFive)
#print(setUnion)

## Checks to see similar elements in sets
# setIntersection = setOne.intersection(setFour)
# print(setIntersection)
#
# setIntersectionTwo = setFour.intersection(setFive)
# print(setIntersectionTwo)

##Difference between sets
setSix = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setSeven = {1, 2, 3, 10, 20, 30}
# setDiff = setSix.difference(setSeven)
# setDiff2 = setSeven.difference(setSix)

# print(setDiff)
# print(setDiff2)

# setSymDiff = setSix.symmetric_difference(setSeven)
# print(setSymDiff) #all the elements that are different between the sets

## Updating sets will not make new space in memory
# setSix.update(setSeven)
# setSix.intersection_update(setSeven)
# setSix.difference_update(setSeven)
# setSix.symmetric_difference_update(setSeven)
# print(setSix)

## Super sets and disjoint methods
# setEight = {1, 2, 3}
# setNine = {1, 2, 3, 10, 20, 30}
# setTen = {5, 6}
# print(setEight.issubset(setNine)) #returns true all elements of first set before .issubset are a subset of set inside parenthesis
# print(setNine.issubset(setEight)) #returns false if all elements of first set before .issubset are NOT a subset of set inside parenthesis
# print(setNine.issuperset(setEight)) #returns true if the first set contains all elements of the second set
# print(setEight.issuperset(setNine)) #returns false if the first set DOES NOT contains all elements of the second set
# print(setTen.isdisjoint(setNine)) #returns true IF there are no similar elements
# print(setNine.isdisjoint(setEight)) #returns false IF there are similar elements

## Follows the copying rules for other types of arrays

## Frozenset cannot change it after its creation makes it immutable like a tuple
setFrozen1 = frozenset([1, 2, 3, 4])