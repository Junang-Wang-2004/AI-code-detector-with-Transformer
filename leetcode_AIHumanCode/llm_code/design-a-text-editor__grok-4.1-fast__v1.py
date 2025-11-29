class TextEditor:
    def __init__(self):
        self.buffer = []
        self.tail = []
        self.view = 10

    def addText(self, text):
        self.buffer.extend(text)

    def deleteText(self, k):
        count = min(k, len(self.buffer))
        del self.buffer[-count:]
        return count

    def cursorLeft(self, k):
        count = min(k, len(self.buffer))
        self.tail.extend(self.buffer[-count:][::-1])
        del self.buffer[-count:]
        return ''.join(self.buffer[-self.view:])

    def cursorRight(self, k):
        count = min(k, len(self.tail))
        self.buffer.extend(self.tail[-count:][::-1])
        del self.tail[-count:]
        return ''.join(self.buffer[-self.view:])
