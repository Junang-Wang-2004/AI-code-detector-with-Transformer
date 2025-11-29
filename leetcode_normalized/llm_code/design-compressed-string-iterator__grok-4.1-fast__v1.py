class C1(object):

    def __init__(self, a1):
        self.s = a1
        self.ptr = 0
        self.letter = ' '
        self.remaining = 0

    def __next__(self):
        if self.remaining == 0:
            if self.ptr >= len(self.s):
                return ' '
            self.letter = self.s[self.ptr]
            self.ptr += 1
            v1 = 0
            while self.ptr < len(self.s) and self.s[self.ptr].isdigit():
                v1 = v1 * 10 + int(self.s[self.ptr])
                self.ptr += 1
            self.remaining = v1
        self.remaining -= 1
        return self.letter

    def hasNext(self):
        return self.remaining > 0 or self.ptr < len(self.s)
