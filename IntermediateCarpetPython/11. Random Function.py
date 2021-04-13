import random
import secrets
import numpy as np

# a = random.random()
# print(a)
#
# b = random.randint(1, 100)
# print(b)
# # upper bound is included
#
# c = random.uniform(1, 10)
# print(c)
#
# d = random.randrange(1, 100, 2)
# # upper bound is not included
# print(d)
#
# e = random.normalvariate(0, 1)
# # statistical normal distribution with mean 0 and standard deviation 1
# print(e)

# listOne = list("ABCDEFGHI")
# print(listOne)
# randomLetter = random.choice(listOne)
# randomLetters = random.sample(listOne, 3) #pick unique elements
# randomLettersAgain = random.choices(listOne, k = 3) #if you don't want to pick unique elements
# random.shuffle(listOne) #shuffle list in place
# print(randomLetter)
# print(randomLetters)
# print(randomLettersAgain)
# print(listOne)

# #random number BUT number is set so that we can reuse these random numbers
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
#
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))
#
# random.seed(3)
# print(random.random())
# print(random.randint(1, 10))
#
# # Since numbers are reproducible do not use for sec purposes.

# # Secrets should be used for tokens, acc verification, etc it takes more time for algos to generate random number
# # Only three functions
# first = secrets.randbelow(10)
# print(first)
#
# second = secrets.randbits(10)
# # bit numbers 1(512) 1(256) 1(128) 1(64) 1(32) 1(16) 1(8) 1(4) 1(2) 1(1)
# print(second)
#
# listOne = list("ABCDEFGH")
# third = secrets.choice(listOne)
# print(third)

# # Numpy functions
# a = np.random.rand(3)
# print(a)
#
# b = np.random.randint(1, 10, 3) #10 is excluded prints a 1D array with three
# c = np.random.randint(1, 10, (4,3)) #10 is excluded prints a 2D array with three
# print(b)
# print(c)
#
# numpyArr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(numpyArr)
#
# np.random.shuffle(numpyArr) #only shuffle elements along first axis SO it is only shuffling arr[THIS ONE][]
# print(numpyArr)
#
# np.random.seed(1)
# print(np.random.rand(3,3))
#
# np.random.seed(2)
# print(np.random.rand(3,3))