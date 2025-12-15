# Problem_Set_1_To_Solve

# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#

# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which
#    should be 10

#
# Your test function should run assertion checks and throw an
# AssertionError for each of the 5 incorrect Queues. Pressing
# submit will tell you how many you successfully catch so far.

#Creating the bolean to make the erreur append or not

import random

Trigger_error1= random.randint(0,1)
Trigger_error2= random.randint(0,1)
Trigger_error3= random.randint(0,1)
Trigger_error4= random.randint(0,1)
Trigger_error5= random.randint(0,1)

#The queue function

import array

class Queue:

    def __init__(self,size_max):

        assert size_max > 0
        if Trigger_error2==1:
            if size_max>15:
                size_max=15

        if Trigger_error5==1:
            size_max-=1

        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):

        if Trigger_error3==1:
         return self.dequeue() is None
        else:
         return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False

        if Trigger_error1==1:
          x=x%(2**16)

        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            if Trigger_error4 ==1:
                return False
            else:
                return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

def test():

  # Error trigger by the code

  if Trigger_error1==1:
     print("The error 1 is triggered")  

  if Trigger_error2==1:
     print("The error 2 is triggered")

  if Trigger_error3==1:
     print("The error 3 is triggered")

  if Trigger_error4==1:
     print("The error 4 is triggered")    

  if Trigger_error5==1:
     print("The error 5 is triggered")

  # Your code here
  # first assertion to be verified
  q= Queue(1) # verify that the queue can contain more than 0 items
  
  # second assertion to be verified
  assert q.empty() == True  # verify that the queue is empty at the beginning
  assert not q.full()  # check that the queue is not full at the start
  
  # third assertion to be verified
  for i in range(20):
      success= q.enqueue(10)
      if i == 0:
          assert success == True  # verify that we can queue items until they are full
      else:
          assert success == False  # verify that it is impossible to add items to the queue when it is full

  # fourth assertion to be verified
  assert q.full() == True  # verify that the queue is full
  
  # fifth assertion to be verified
  value= q.dequeue()
  assert value ==10 # verify that an element can be dequeued when the queue is not empty
  # Calling my test function

test()
