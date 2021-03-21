import sys
import timeit
## Tuple: ordered, immutable used for objects that belong together
## Can access Tuple with an index number
tupleOne = ("Joe", 27, "Colorado Springs")
#print(tupleOne[1])
#can use a for loop to iterate through the tuple

# if "JOE" in tupleOne:
#     print("Yes")
# else:
#     print("NO")

tupleTwo = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(len(tupleTwo)) #length of the tuple
# print(tupleTwo.count('a')) #counts how many of an element is in the tuple
# print(tupleTwo.index('b')) #returns first occurrence of what is being searched for
#
# #tuple to list
# listTupleTwo = list(tupleTwo)
# print(listTupleTwo)
#
# #list to tuple
# tupleThree = tuple(listTupleTwo)
# print(tupleThree)

# tupleSlice = tupleTwo[1:9] #last index is not included #same as lists
# tupleStep = tupleTwo[::3] #step and get every third element
# print(tupleSlice)
# print(tupleStep)

##Unpacking elements
# name, age, city = tupleOne
# print(name)
# print(age)
# print(city)

tupleThree = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = tupleThree # *i2 grabs all items up to i2 so 1-4
print(i1)
print(i3)
print(i2)

##Comparing tuples and lists
listComp = [1, 2, 3, 4, "hello", True]
tupleComp = (1, 2, 3, 4, "hello", True)
print(sys.getsizeof(listComp), "bytes") #list is larger even with same elements
print(sys.getsizeof(tupleComp), "bytes") #tuple is more efficient to iterate through

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=100000)) #list is slower  0.004 to create 1mil instances
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=100000)) #tuple is faster to generating a tuple 0.0008