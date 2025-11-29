class C1(object):

    def __init__(self):
        self.q_ = Queue()
        self.top_ = None

    def push(self, a1):
        self.q_.push(a1)
        self.top_ = a1

    def pop(self):
        for v1 in range(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        return self.q_.pop()

    def top(self):
        return self.top_

    def empty(self):
        return self.q_.empty()
