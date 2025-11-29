class C1(object):

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, a1):
        if not self.stack:
            self.stack.append(0)
            self.min = a1
        else:
            self.stack.append(a1 - self.min)
            if a1 < self.min:
                self.min = a1

    def pop(self):
        v1 = self.stack.pop()
        if v1 < 0:
            self.min = self.min - v1

    def top(self):
        v1 = self.stack[-1]
        if v1 > 0:
            return v1 + self.min
        else:
            return self.min

    def getMin(self):
        return self.min
