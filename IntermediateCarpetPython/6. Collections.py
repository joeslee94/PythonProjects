# collections: counter, namedtuple, orderedDict, dedaultDict, deque
from collections import Counter
from collections import *
# # IF we want to count the number of elements in the string
# a = "aaaaaaaaabbbbbbbcccc"
# counterOne = Counter(a)
# print(counterOne.items())
# print(counterOne.keys())
# print(counterOne.values())
# print(counterOne.most_common(1)[0][0])
# # returns list with tuples. put the number of how many most common elements I want to see
# # if I only want to see the element such as "a" then I need to access it
# # index 0 of the list AND index 0 of the tuple
# # can use a list or any other iterables
# print(list(counterOne.elements()))

# # namedTuple
# point = namedtuple('point', 'x,y')
# pointOne = point(1, -4)
# print(pointOne)
# print(pointOne.x, pointOne.y)

## OrderedDicts
# orderedDictOne = OrderedDict()
# orderedDictOne['g'] = 7
# orderedDictOne['a'] = 1
# orderedDictOne['b'] = 2
# orderedDictOne['c'] = 3
# orderedDictOne['d'] = 4
# orderedDictOne['e'] = 5
# orderedDictOne['f'] = 6
# print(orderedDictOne)

## default Dicts
# defaultDictOne = defaultdict(int)
# defaultDictOne['a'] = 1
# defaultDictOne['b'] = 2
# print(defaultDictOne[3])
# # Returns default type of the element type we specified

## deque removes from both ends
dequeOne = deque()

dequeOne.append(1)
dequeOne.append(2)
dequeOne.append(3)
print(dequeOne)

dequeOne.appendleft(4)
dequeOne.appendleft(5)
dequeOne.appendleft(6)
print(dequeOne)

dequeOne.pop()
print(dequeOne)

dequeOne.popleft()
print(dequeOne)

dequeOne.extend([0, 9, 8]) #goes in 0, 9, 8
print(dequeOne)

dequeOne.extendleft([0, 9, 1]) #goes in 0, 9 , 1
print(dequeOne)

dequeTwo = deque()
dequeTwo.extend([1, 2, 3, 4, 5])
dequeTwo.rotate() #produces 5, 1, 2, 3, 4 so bumps left element to the front
dequeTwo.rotate(-1) #bumps first element to the back of the list
print(dequeTwo)