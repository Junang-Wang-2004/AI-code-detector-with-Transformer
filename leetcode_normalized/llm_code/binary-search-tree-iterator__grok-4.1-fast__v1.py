class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = self.right = None

class C2(object):

    def __init__(self, a1):
        self.path = []
        v1 = a1
        while v1:
            self.path.append(v1)
            v1 = v1.left

    def hasNext(self):
        return len(self.path) > 0

    def __next__(self):
        v1 = self.path.pop()
        v2 = v1.right
        while v2:
            self.path.append(v2)
            v2 = v2.left
        return v1.val
