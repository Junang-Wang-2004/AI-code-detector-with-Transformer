class C1:

    def __init__(self, a1):
        self.capacity = a1
        self.data = [0] * a1
        self.total = 0
        self.current = 0
        self.ptr = 0

    def next(self, a1):
        if self.current == self.capacity:
            self.total -= self.data[self.ptr]
        else:
            self.current += 1
        self.data[self.ptr] = a1
        self.total += a1
        self.ptr = (self.ptr + 1) % self.capacity
        return self.total / self.current
