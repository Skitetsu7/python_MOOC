# TASK:
#
# Achieve full statement coverage on the Queue class. 
# You will need to:
# 1) Write your test code in the test function.
# 2) Use python3-coverage package to test coverage.
#    CLI: coverage erase ;
#         coverage run Problem_Set_2_1.py ;
#         coverage html -i
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Add test code to test() that achieves 100% coverage of the 
# Queue class.
def test():
    ### Your code here
    x = Queue(2) #create a queue, coverage init function
    assert x.empty() #coverage on the empty function
    full = x.full()
    assert not full #coverage on the full function
    dequeue = x.dequeue() #for the coverage of the first return I need to dequeue an empty queue with the dequeue function
    assert dequeue is None
    x.checkRep() #check coverage of the firsts assert
    
    success = x.enqueue(17) #coverage on the enqueue function, except "if self.tail == self.max:" in the function
    assert success
    x.checkRep() #check coverage of the 4 firsts assert
    
    success = x.enqueue(24) # application of the coverage on this condition : "if self.tail == self.max:"
    assert success
    success = x.enqueue(5) #check the enqueue function when the queue is full, coverage the first return of the function
    assert not success
    dequeue = x.dequeue() #coverage on the dequeue function, except "if self.tail == self.max:" in the function
    assert dequeue == 17
    x.checkRep()
    
    dequeue = x.dequeue() # application of the coverage on this condition : "if self.tail == self.max:"
    assert dequeue == 24
    
    dequeue = x.dequeue() #verify the condition when we want dequeue an empty queue
    assert dequeue is None
    empty = x.empty() #verify that the queue is empty after remove the elements
    assert empty
    x.checkRep() #last check, head and tail include in the queue
test()
