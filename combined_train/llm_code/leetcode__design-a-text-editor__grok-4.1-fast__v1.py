class C1:

    def __init__(self):
        self.buffer = []
        self.tail = []
        self.view = 10

    def addText(self, a1):
        self.buffer.extend(a1)

    def deleteText(self, a1):
        v1 = min(a1, len(self.buffer))
        del self.buffer[-v1:]
        return v1

    def cursorLeft(self, a1):
        v1 = min(a1, len(self.buffer))
        self.tail.extend(self.buffer[-v1:][::-1])
        del self.buffer[-v1:]
        return ''.join(self.buffer[-self.view:])

    def cursorRight(self, a1):
        v1 = min(a1, len(self.tail))
        self.buffer.extend(self.tail[-v1:][::-1])
        del self.tail[-v1:]
        return ''.join(self.buffer[-self.view:])
