class C1:

    def __init__(self):
        self.values = []
        self.minimums = []

    def push(self, a1):
        self.values.append(a1)
        if not self.minimums or a1 <= self.minimums[-1]:
            self.minimums.append(a1)

    def pop(self):
        if self.values and self.values[-1] == self.minimums[-1]:
            self.minimums.pop()
        self.values.pop()

    def top(self):
        return self.values[-1]

    def getMin(self):
        return self.minimums[-1]
