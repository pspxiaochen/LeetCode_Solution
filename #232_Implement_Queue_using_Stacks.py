class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
    def push(self,x):
        self.input.append(x)
    def pop(self):
        self.peek()
        return self.output.pop()
    def peek(self):
        if self.output == []:
            while (self.input != []):
                self.output.append(self.input.pop())
        return self.output[-1]
    def empty(self):
        return self.output == [] and self.input == []