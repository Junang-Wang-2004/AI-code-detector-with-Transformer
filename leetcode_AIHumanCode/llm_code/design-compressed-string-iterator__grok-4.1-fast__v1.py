class StringIterator(object):

    def __init__(self, compressedString):
        self.s = compressedString
        self.ptr = 0
        self.letter = ' '
        self.remaining = 0

    def __next__(self):
        if self.remaining == 0:
            if self.ptr >= len(self.s):
                return ' '
            self.letter = self.s[self.ptr]
            self.ptr += 1
            count = 0
            while self.ptr < len(self.s) and self.s[self.ptr].isdigit():
                count = count * 10 + int(self.s[self.ptr])
                self.ptr += 1
            self.remaining = count
        self.remaining -= 1
        return self.letter

    def hasNext(self):
        return self.remaining > 0 or self.ptr < len(self.s)
