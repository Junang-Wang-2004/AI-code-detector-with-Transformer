class MovingAverage:

    def __init__(self, size):
        self.capacity = size
        self.data = [0] * size
        self.total = 0
        self.current = 0
        self.ptr = 0

    def next(self, val):
        if self.current == self.capacity:
            self.total -= self.data[self.ptr]
        else:
            self.current += 1
        self.data[self.ptr] = val
        self.total += val
        self.ptr = (self.ptr + 1) % self.capacity
        return self.total / self.current
