##Making a list
listOne = ["Item1", "Item2", "Item3", 4, 5, 6, 7, 8, 9, 10]

##step list
# print(listOne[::1])
# print(listOne[::2])
# print(listOne[::3])

##can use pop to take off the last item off
# lastItem = listOne.pop()
# print(f"{listOne} lastitem: {lastItem}")

##sort, reverse, and other methods can be called
# listOne.sort()
# listOne.reverse()
# listOne.copy() #remember when copying lists you cant equate the copy list to the org list BECAUSE it'll copy the memory location

##if I want 1 value repeated in a list and stored in a list
# listTwo = [0] * 7
# print(listTwo)

##Concatenate two lists
# longList = listOne + listTwo
# print(longList)

##slicing list, if you dont specify start index, it'll begin at item[0] and no stop index go to item[len(List)]
# print(longList[1:5])

listOfNums = [1, 2, 3, 4, 6, 7, 8]
listOfSquaredNums = [i * i for i in listOfNums]
print(f"Original: {listOfNums}\n"
      f"Squared: {listOfSquaredNums}")