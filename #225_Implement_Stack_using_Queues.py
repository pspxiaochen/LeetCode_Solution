import collections
class MyStack(object):
    def __init__(self):
        self.stack = collections.deque()

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0