class C1:

    def __init__(self):
        self.buffer = [''] * 4
        self.ptr = 0
        self.length = 0

    def read(self, a1, a2):
        v1 = 0
        while v1 < a2:
            if self.ptr < self.length:
                v2 = self.length - self.ptr
                v3 = min(v2, a2 - v1)
                a1[v1:v1 + v3] = self.buffer[self.ptr:self.ptr + v3]
                self.ptr += v3
                v1 += v3
                continue
            self.length = read4(self.buffer)
            if self.length == 0:
                return v1
            self.ptr = 0
        return v1
