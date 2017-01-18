class Stack():
    def __init__(self, max_size=20):
        self.max_size = max_size
        self.data = [-1]*max_size
        self.top = 0
    @property
    def is_empty(self):
        if self.top <= 0:
            return True
        return False
    def push(self,x):
        if self.top >= self.max_size:
            raise Exception("stack is full")
        self.data[self.top] = x
        self.top += 1
    def pop(self):
        if self.top <= 0:
            raise Exception("stack is empty")
        r = self.data[self.top-1]
        self.top -= 1
        return r
    def __str__(self):
        return str(self.data[:self.top])
#
# stack = Stack()
# # for i in xrange(20):
# #     stack.push(i)
# print stack.pop()
# print stack