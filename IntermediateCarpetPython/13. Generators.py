import sys
# def generatorOne():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# # can't use generator independently
# # example, if sum is called on generator, I cannot sort the generator
# # I cannot sequence the generator from top to bottom
# g = generatorOne()

# for i in g:
#     print(i)

# prints using the next function
# value = next(g)
# print(value)
#
# value = next(g)
# print(value)
#
# value = next(g)
# print(value)
#
# value = next(g)
# print(value)
#
# value = next(g)
# print(value)

# print(sum(g))
# print(sorted(g))

# def generatorTwo(num):
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1
#     print("Complete")
#
# countDown = generatorTwo(5)
# value = next(countDown)
# print(value)
#
# value = next(countDown)
# print(value)
#
# value = next(countDown)
# print(value)
#
# value = next(countDown)
# print(value)
#
# value = next(countDown)
# print(value)
#
# value = next(countDown)
# print(value)

# def upToNum(num):
#     nums = []
#     numOne = 0
#     while(num > numOne):
#         nums.append(numOne)
#         numOne += 1
#     return nums
#
# print(upToNum(10))
# print(sum(upToNum(10)))
#
# def upToNumGenerator(num):
#     numOne = 0
#     while num > numOne:
#         yield numOne
#         numOne +=1
#
# print(list(upToNumGenerator(10)))
# print(sum(upToNumGenerator(10)))
#
# # Generator is much smaller than a list holding items

#limit is the number at which to stop
# def fibonacci(limit):
#     # 0, 1, 1, 2, 3, 5, 8
#     numOne = 0
#     numTwo = 1
#     while numOne < limit:
#         yield numOne
#         numOne, numTwo = numTwo, numOne + numTwo
#
# fib = fibonacci(30)
# for i in fib:
#     print(i)

generatorOne = (i for i in range(10) if i % 2 == 0)
print(list(generatorOne))
# for i in generatorOne:
#     print(i)

listComprehension = [i for i in range(10) if i % 2 == 0]
print(listComprehension)
