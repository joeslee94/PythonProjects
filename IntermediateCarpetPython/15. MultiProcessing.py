import time
from multiprocessing import *
import os
import time

# def squareNums():
#     for i in range(12):
#         i*i

# if __name__ == "__main__":
#     processes = []
#     numProcesses = os.cpu_count()
#     #print(numProcesses) #12 CPUs
#
#     #create processes
#     for i in range(numProcesses):
#         p = Process(target=squareNums())
#         processes.append(p)
#
#     #start
#     for p in processes:
#         p.start()
#
#     #join
#     for p in processes:
#         p.join()
#
#     #Only reach this point when all processes are complete
#     print("End Main")

# CREATING AND MANAGING PROCESSES
# def add_100(numbers, lock):
    # with lock:
    #     for i in range(100):
    #         #number.value += 1 #(for shared num)
    #         for i in range(len(numbers)): #(for shared arrays)
    #             numbers[i] += 1

# Queue process safe exchanges
# def squareNums(numbers, queueOne):
#     for i in numbers:
#         queueOne.put(i * i)
#
# def makeNegative(numbers, queueOne):
#     for i in numbers:
#         queueOne.put(-1*i)

def cube(number):
    return number * number * number

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()

    result = pool.map(cube, numbers)
    pool.close()
    pool.join()

    print(result)

    # WORKING WITH QUEUE
    # queueOne = Queue()
    # numbers = range(1, 6)
    #
    # p1 = Process(target=squareNums, args=(numbers, queueOne))
    # p2 = Process(target=makeNegative, args=(numbers, queueOne))
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()
    #
    # while not queueOne.empty():
    #     print(queueOne.get())

    # CREATING AND MANAGING PROCESSES
    # shared_number = Value('i', 0)
    # lock = Lock()
    # sharedArray = Array('d', [0.0, 100.0, 200.0, 300.0])
    # print('Array at the beginning is ', sharedArray[:])
    # # print('Number at the beginning is ', shared_number.value)
    #
    # p1 = Process(target=add_100, args=(sharedArray, lock))
    # p2 = Process(target=add_100, args=(sharedArray, lock))
    # # p1 = Process(target=add_100, args=(shared_number, lock))
    # # p2 = Process(target=add_100, args=(shared_number, lock))
    # # both processes tried to read and write into the same time of add_100
    # # to prevent this we need a lock to prevent this
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()
    #
    # print('Array at the end is ', sharedArray[:])
    # # print('number at end is ', shared_number.value)