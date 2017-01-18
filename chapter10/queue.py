class Queue():
    def __init__(self, max_size=20):
        self.max_size = max_size
        self.data = [-1]*max_size
        self.head = 0
        self.tail = 0

    def incre(self, i):
        if i >= self.max_size - 1:
            return 0
        return i+1

    @property
    def is_empty(self):
        return self.tail == self.head

    def enqueue(self,x):
        if self.incre(self.tail) == self.head:
            raise Exception("queue is full")
        self.data[self.tail] = x
        self.tail = self.incre(self.tail)

    def dequeue(self):
        if self.tail == self.head:
            raise Exception("queue is empty")
        r = self.data[self.head]
        self.head = self.incre(self.head)
        return r

    def __str__(self):
        if self.tail == self.head:
            return str([])
        if self.tail > self.head:
            return str(self.data[self.head:self.tail])
        else:
            first_half = self.data[self.head:self.max_size]
            second_half = self.data[:self.tail]
            return str(first_half+second_half)
#
# queue = Queue()
# print queue
# for i in xrange(20):
#     queue.enqueue(i)
#     print i, queue,queue.head,queue.tail
#
# print queue.head, queue.tail
# print queue
# for i in xrange(20):
#     print queue.dequeue(),queue,queue.head,queue.tail
# print queue