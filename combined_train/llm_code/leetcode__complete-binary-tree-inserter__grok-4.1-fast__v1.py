from collections import deque

class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def __init__(self, a1):
        self.root = a1
        self.ready = deque()
        v1 = deque([a1])
        while v1:
            v2 = v1.popleft()
            if v2.left is None or v2.right is None:
                self.ready.append(v2)
            if v2.left:
                v1.append(v2.left)
            if v2.right:
                v1.append(v2.right)

    def insert(self, a1):
        v1 = self.ready[0]
        v2 = C1(a1)
        if v1.left is None:
            v1.left = v2
        else:
            v1.right = v2
            self.ready.popleft()
        self.ready.append(v2)
        return v1.val

    def get_root(self):
        return self.root
