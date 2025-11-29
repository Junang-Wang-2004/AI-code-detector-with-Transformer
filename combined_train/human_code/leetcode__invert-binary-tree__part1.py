import collections

class C1(object):

    def __init__(self):
        self.data = collections.deque()

    def push(self, a1):
        self.data.append(a1)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

class C2(object):

    def invertTree(self, a1):
        if a1 is not None:
            v1 = C1()
            v1.push(a1)
            while not v1.empty():
                v2 = v1.pop()
                v2.left, v2.right = (v2.right, v2.left)
                if v2.left is not None:
                    v1.push(v2.left)
                if v2.right is not None:
                    v1.push(v2.right)
        return a1
