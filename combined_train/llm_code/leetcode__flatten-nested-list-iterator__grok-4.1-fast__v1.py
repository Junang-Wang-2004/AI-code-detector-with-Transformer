class C1:

    def __init__(self, a1):
        self.stack = [(a1, 0)]

    def __next__(self):
        v1, v2 = self.stack[-1]
        self.stack.pop()
        v3 = v1[v2].getInteger()
        self.stack.append((v1, v2 + 1))
        return v3

    def hasNext(self):
        while self.stack:
            v1, v2 = self.stack[-1]
            if v2 == len(v1):
                self.stack.pop()
                continue
            if v1[v2].isInteger():
                return True
            self.stack.pop()
            v3 = v1[v2].getList()
            self.stack.append((v1, v2 + 1))
            self.stack.append((v3, 0))
        return False
