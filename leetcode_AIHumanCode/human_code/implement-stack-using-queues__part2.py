# Time: push: O(1), pop: O(n), top: O(1)
# Space: O(n)
class Stack2(object):
    # initialize your data structure here.
    def __init__(self):
        self.q_ = Queue()
        self.top_ = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q_.push(x)
        self.top_ = x

    # @return nothing
    def pop(self):
        for _ in range(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        return self.q_.pop() 

    # @return an integer
    def top(self):
        return self.top_

    # @return an boolean
    def empty(self):
        return self.q_.empty()

