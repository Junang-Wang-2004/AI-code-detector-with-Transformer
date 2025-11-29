class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [(nestedList, 0)]

    def __next__(self):
        current, index = self.stack[-1]
        self.stack.pop()
        value = current[index].getInteger()
        self.stack.append((current, index + 1))
        return value

    def hasNext(self):
        while self.stack:
            current, index = self.stack[-1]
            if index == len(current):
                self.stack.pop()
                continue
            if current[index].isInteger():
                return True
            self.stack.pop()
            sub = current[index].getList()
            self.stack.append((current, index + 1))
            self.stack.append((sub, 0))
        return False
