class C1:

    def __init__(self, a1):
        self.ptr = 0
        self.data = [None] * a1

    def insert(self, a1, a2):
        a1 -= 1
        self.data[a1] = a2
        v2 = []
        while self.ptr < len(self.data) and self.data[self.ptr] is not None:
            v2.append(self.data[self.ptr])
            self.ptr += 1
        return v2
