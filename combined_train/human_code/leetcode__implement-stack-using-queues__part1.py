import collections

class C1(object):

    def __init__(self):
        self.data = collections.deque()

    def push(self, a1):
        self.data.append(a1)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

class C2(object):

    def __init__(self):
        self.q_ = C1()

    def push(self, a1):
        self.q_.push(a1)
        for v1 in range(self.q_.size() - 1):
            self.q_.push(self.q_.pop())

    def pop(self):
        self.q_.pop()

    def top(self):
        return self.q_.peek()

    def empty(self):
        return self.q_.empty()
