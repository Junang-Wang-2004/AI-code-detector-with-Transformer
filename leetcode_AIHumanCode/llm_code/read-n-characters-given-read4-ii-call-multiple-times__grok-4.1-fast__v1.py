class Solution:
    def __init__(self):
        self.buffer = [""] * 4
        self.ptr = 0
        self.length = 0

    def read(self, target, size):
        copied = 0
        while copied < size:
            if self.ptr < self.length:
                remaining = self.length - self.ptr
                chunk = min(remaining, size - copied)
                target[copied:copied + chunk] = self.buffer[self.ptr:self.ptr + chunk]
                self.ptr += chunk
                copied += chunk
                continue
            self.length = read4(self.buffer)
            if self.length == 0:
                return copied
            self.ptr = 0
        return copied
