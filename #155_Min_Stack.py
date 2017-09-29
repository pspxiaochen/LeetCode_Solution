import sys
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        self.a.append((x, min(self.getMin(), x)))

    def pop(self):
        del self.a[-1]

    def top(self):
        if self.a:
            return self.a[-1]

    def getMin(self):
        if self.a:
            return self.a[-1][1]
        return sys.maxint