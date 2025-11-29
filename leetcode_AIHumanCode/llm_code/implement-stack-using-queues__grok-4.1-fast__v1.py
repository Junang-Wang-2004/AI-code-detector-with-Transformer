import collections


class Stack:
    def __init__(self):
        self.buffer = collections.deque()

    def push(self, x):
        self.buffer.append(x)
        self.buffer.rotate(1)

    def pop(self):
        return self.buffer.popleft()

    def top(self):
        return self.buffer[0]

    def empty(self):
        return len(self.buffer) == 0
