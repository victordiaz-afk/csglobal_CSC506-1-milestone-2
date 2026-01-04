# Module: funtionality_test
# Purpose: Quick smoke tests to exercise Stack, Deque, LinkedList and Queue implementations.
# Notes:
# - Randomized tests; prints results for manual inspection.
# - Constants at top control test sizes and delete counts.

from data_types.queue import Queue
from data_types.dequeue import Deque
from data_types.stack import Stack
from data_types.linked_list import LinkedList
import random


TEST_CASE = 20
DELETE_NUMBER = 10
SEARCH_NUMBER = random.randint(0, TEST_CASE)

print("\n================ Functionality Testing (Stack) ================")
print(f"\n======= Pushing {TEST_CASE} data points onto Stack ================")
test_stack = Stack()

for i in range(TEST_CASE):
    test_stack.push(random.randint(0, TEST_CASE))

print(f"\n======= Checking if Stack is empty ================")
if test_stack.isEmpty():
    print("Stack is empty.")
else:
    print("Stack is not empty.")

print(f"\n======= Peeking at the top of the Stack ================")
print(test_stack.peek())

print(f"\n======= Popping {DELETE_NUMBER} items from Stack ================")
for i in range(DELETE_NUMBER):
    test_stack.pop()

print(f"\n======= Peeking at the Stack again ================")
print(test_stack.peek())



print("\n================ Functionality Testing (Deque) ================")
print(f"\n======= Adding {TEST_CASE/2} data points to the FRONT of the Deque ================")
test_dequeue = Deque()

for i in range(int(TEST_CASE/2)):
    test_dequeue.addFront(random.randint(0, int(TEST_CASE/2)))

test_dequeue.display()

print("\n================ Functionality Testing (Deque) ================")
print(f"\n======= Adding {TEST_CASE/2} data points to the back  of the Deque ================")
for i in range(int(TEST_CASE/2)):
    test_dequeue.addRear(random.randint(0, TEST_CASE))

test_dequeue.display()

print(f"\n======= Checking if Deque is empty ================")
if test_dequeue.isEmpty():
    print("Deque is empty.")
else:
    print("Deque is not empty.")



print(f"\n======= Removing {DELETE_NUMBER/2} items from the FRONT of the Deque ================")
for i in range(int(DELETE_NUMBER/2)):
    test_dequeue.removeFront()

print(f"\n======= Displaying Deque again ================")
test_dequeue.display()

print(f"\n======= Removing {DELETE_NUMBER/2} items from the BACK of the Deque ================")
for i in range(int(DELETE_NUMBER/2)):
    test_dequeue.removeRear()
print(f"\n======= Checking the of the Deque ================")
test_dequeue.display()


print("\n================ Functionality Testing (LinkedList) ================")
test_link = LinkedList()

print(f"\n======= Adding {TEST_CASE} data points to LinkedList ================")
for i in range(TEST_CASE):
    test_link.insert(random.randint(0, TEST_CASE))

test_link.display()

print(f"\n======= Deleting {DELETE_NUMBER} data points from LinkedList ================")
for i in range(DELETE_NUMBER):
    test_link.delete()

print(f"\n======= Searching for {SEARCH_NUMBER} in LinkedList ================")
num = test_link.search(SEARCH_NUMBER)
if num is None:
    print(f"{SEARCH_NUMBER} was NOT found in the LinkedList.")
else:
    print(f"{SEARCH_NUMBER} WAS found in the LinkedList.")

print("\n======= Printing LinkedList ================")
test_link.display()



print("\n================ Functionality Testing (Queue) ================")
print("\n================ Functionality Testing (Deque) ================")
