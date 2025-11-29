class MinStack:
    def __init__(self):
        self.values = []
        self.minimums = []

    def push(self, num):
        self.values.append(num)
        if not self.minimums or num <= self.minimums[-1]:
            self.minimums.append(num)

    def pop(self):
        if self.values and self.values[-1] == self.minimums[-1]:
            self.minimums.pop()
        self.values.pop()

    def top(self):
        return self.values[-1]

    def getMin(self):
        return self.minimums[-1]
