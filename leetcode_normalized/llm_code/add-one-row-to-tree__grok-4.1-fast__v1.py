from collections import deque

class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def addOneRow(self, a1, a2, a3):
        if a3 == 1:
            v1 = C1(a2)
            v1.left = a1
            return v1
        if a3 == 0:
            v1 = C1(a2)
            v1.right = a1
            return v1
        if a1 is None:
            return a1
        v2 = deque([(a1, 1)])
        while v2:
            v3, v4 = v2.popleft()
            if v4 == a3 - 1:
                v5 = v3.left
                v3.left = C1(a2)
                v3.left.left = v5
                v6 = v3.right
                v3.right = C1(a2)
                v3.right.right = v6
                continue
            if v3.left is not None:
                v2.append((v3.left, v4 + 1))
            if v3.right is not None:
                v2.append((v3.right, v4 + 1))
        return a1
