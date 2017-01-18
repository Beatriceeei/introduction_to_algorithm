from stack import Stack

class Queue():
    def __init__(self):
        self.stack1 = Stack()#responsable for dequeue
        self.stack2 = Stack()#responsable for enqueue
    def dequeue(self):
        if self.stack1.is_empty:
            while not self.stack2.is_empty:
                self.stack1.push(self.stack2.pop())
            return self.stack1.pop()
        else:
            return self.stack1.pop()
    def enqueue(self,x):
        if self.stack1.is_empty:
            self.stack2.push(x)
        else:
            while not self.stack1.is_empty:
                self.stack2.push(self.stack1.pop())
            self.stack2.push(x)

queue = Queue()
for i in xrange(5):
    queue.enqueue(i)
print queue.stack1,queue.stack2
print queue.dequeue()
print queue.stack1, queue.stack2
print queue.dequeue()
print queue.stack1, queue.stack2
queue.enqueue(6)
print queue.dequeue()