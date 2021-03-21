from timeit import default_timer as timer
# ##string : ordered, immutable, text representation
# stringOne = """Hello World"""
#
# stringTwo = "Hello \nWorld"
#
# stringThree = 'Hello World'
#
# print(stringOne)
# print(stringTwo)
# print(stringThree)
#
stringFour = "01234567"
# charOne = stringFour[0]
# print(charOne)
#
# ## cannot change the character using the index however
#
# ## Slicing same rules as before
# subStringOne = stringFour[:5]
# print(subStringOne)
#
# ## Stepping through
# subStringTwo = stringFour[::-1]
# print(subStringTwo)
#
# ## Concat string
# concatString = f"{stringFour} + {stringFour}"
# print(concatString)

## print all letters in string
for i in stringFour:
    print(i)

## checking if there is a value in the string
if "0234" in stringFour:
    print("True")
else:
    print("False")

## getting rid of white space
stringFive = "              White Space             "
stringFive = stringFive.strip()

##upper case or lower case
stringFive.upper()
stringFive.lower()

##starts with, ends with
stringFive.endswith("e")
stringFive.startswith("W")

##finds the first index that we are looking for
stringFive.find("hit")

#can count the occurences of a certain letter
print(stringFive.count("e"))

##replace characters or substrings
print(stringFive.replace("White", "Black"))
# if it cannot find the item we are asking it to replace, it will return original

## string to array or list, we need to pass in where we want it to split
stringSix = "How are you doing"
stringToListOne = stringSix.split(" ")
print(stringToListOne)

## if we want to go back to string
stringSeven = " ".join(stringToListOne)
print(stringSeven)

# Example from list to join
start = timer()
listTwo = ['b'] * 6
stringEight = "".join(listTwo)
stop = timer()
print(f"{stop - start}")

## formatting the strings
#use f strings that is all
