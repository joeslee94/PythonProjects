import time
from multiprocessing import Process
from threading import *
from queue import *
import os
import time
#
# def squareNums():
#     for i in range(100):
#         i*i
#
# if __name__ == "__main__":
#     threads = []
#     numThreads = os.cpu_count()
#     #print(numProcesses) #12 CPUs
#
#     #create processes
#     for i in range(numThreads):
#         t = Thread(target=squareNums())
#         threads.append(t)
#
#     #start
#     for t in threads:
#         t.start()
#
#     #join
#     for t in threads:
#         t.join()
#
#     #Only reach this point when all processes are complete
#     print("End Main")

# databaseValue = 0
#
# def increase(lock):
#     global databaseValue
#
#     with lock:
#         #lock.acquire()
#         localCopy = databaseValue
#
#         localCopy += 1
#
#         databaseValue = localCopy
#         #lock.release()
#
# if __name__ == "__main__":
#
#     lock = Lock()
#     print('start value', databaseValue)
#
#     thread1 = Thread(target = increase, args=(lock, ))
#     thread2 = Thread(target = increase, args=(lock, ))
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#     print('end value', databaseValue)
#
#     print('end main')

# Queue
# firstQueue = Queue()
# firstQueue.put(1)
# firstQueue.put(2)
# firstQueue.put(3)
#
# firstDequeue = firstQueue.get()
# print(firstDequeue)
#
# firstQueue.task_done()
# firstQueue.join()

def worker(firstQueue, lock):
    while True:
        valueDequeue = firstQueue.get()
        with lock:
            print(f'{current_thread().name} has {valueDequeue} value\n')
        firstQueue.task_done()

if __name__ == "__main__":
    firstQueue = Queue()
    lock = Lock()
    numThreads = 10

    for i in range(numThreads):
        thread = Thread(target=worker, args=(firstQueue, lock))
        thread.daemon = True
        # background/daemon thread when main thread dies
        thread.start()

    for i in range(1, 21):
        firstQueue.put(i)

    firstQueue.join()

    print('end main')

# no lock, threads seem to be paired as they become available with a value
# with lock they print in order