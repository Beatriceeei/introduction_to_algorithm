from queue import Queue

class Stack():
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    def pop(self):
        if self.queue1.is_empty:
            while True:
                r = self.queue2.dequeue()
                if self.queue2.is_empty:
                    return r
                self.queue1.enqueue(r)
        else:
            while True:
                r = self.queue1.dequeue()
                if self.queue1.is_empty:
                    return r
                self.queue2.enqueue(r)
    def push(self,x):
        if self.queue1.is_empty:
            self.queue2.enqueue(x)
        else:
            self.queue1.enqueue(x)

stack = Stack()
for i in xrange(5):
    stack.push(i)
print stack.queue1, stack.queue2
print stack.pop()
print stack.queue1, stack.queue2
print stack.pop()
print stack.queue1, stack.queue2
stack.push(6)
print stack.pop()
