# #Dictionaries Key Value Pairs, Unordered, Mutable
dictOne = {"name": "Joe", "age": 27, "city": "COS"}
# print(dictOne)
#
# #Another way to create a dict
dictTwo = dict(name = "Mary", age = 29, city = "Boston")
# print(dictTwo)
#
# nameValue = dictOne["name"]
# ageValue = dictOne["age"]
# cityValue = dictOne["city"]
# print(f"{nameValue}, {ageValue}, {cityValue}")
#
# #Adding key value pair
# dictOne["email"] = "joe@xyz.com"
# print(dictOne)

#Deleting key value pair
# del dictOne["name"]
# dictOne.popitem()
# print(dictOne)

#Using if try/except statements to print certain elements
# if "name" in dictOne:
#     print(dictOne["name"])
#
# try:
#     print(dictOne["name"])
# except:
#     print("ERROR")

# for key in dictOne:
#     print(key)
#
# for key in dictOne.keys():
#     print(key)
#
# for value in dictOne.values():
#     print(value)
#
# for key, value in dictOne.items():
#     print(key, value)

##Copy rules need to be obeyed if you modify the copy you will be modifying the original

## Merging dictionaries the original keys will be overriden
# dictOne.update(dictTwo)
# print(dictOne)

## Possible key types
## use numbers, tuples, etc
## CANNOT USE THE LIST BECAUSE IT IS MUTABLE
# dictThree = {3: 9, 6: 36, 9: 81}
# print(dictThree)
#
# value = dictThree[6] #put in the actual value of the key
# print(value)

tupleOne = (8, 7)
dictFour = {tupleOne: 15}
print(dictFour[tupleOne])