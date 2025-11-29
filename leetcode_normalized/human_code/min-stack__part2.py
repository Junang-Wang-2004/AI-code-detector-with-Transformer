class C1(object):

    def __init__(self):
        self.stack, self.minStack = ([], [])

    def push(self, a1):
        self.stack.append(a1)
        if len(self.minStack):
            if a1 < self.minStack[-1][0]:
                self.minStack.append([a1, 1])
            elif a1 == self.minStack[-1][0]:
                self.minStack[-1][1] += 1
        else:
            self.minStack.append([a1, 1])

    def pop(self):
        v1 = self.stack.pop()
        if v1 == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1][0]

class C2(object):

    def __init__(self):
        self.stack = []

    def push(self, a1):
        if self.stack:
            v1 = min(a1, self.stack[-1][0])
            self.stack.append((v1, a1))
        else:
            self.stack.append((a1, a1))

    def pop(self):
        return self.stack.pop()[1]

    def top(self):
        return self.stack[-1][1]

    def getMin(self):
        return self.stack[-1][0]
