class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def __init__(self, a1):
        self.sequence = []
        v1 = []
        v2 = a1
        while v2 or v1:
            while v2:
                v1.append(v2)
                v2 = v2.left
            v2 = v1.pop()
            self.sequence.append(v2.val)
            v2 = v2.right
        self.pointer = -1

    def hasNext(self):
        return self.pointer < len(self.sequence) - 1

    def __next__(self):
        self.pointer += 1
        return self.sequence[self.pointer]

    def hasPrev(self):
        return self.pointer > 0

    def prev(self):
        self.pointer -= 1
        return self.sequence[self.pointer]
