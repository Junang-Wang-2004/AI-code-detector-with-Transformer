from collections import deque

class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def reverseOddLevels(self, a1):
        if not a1:
            return a1
        v1 = deque([a1])
        v2 = 0
        while v1:
            v3 = len(v1)
            v4 = []
            for v5 in range(v3):
                v4.append(v1.popleft())
            if v2 % 2 == 1:
                v6 = 0
                v7 = v3 - 1
                while v6 < v7:
                    v4[v6].val, v4[v7].val = (v4[v7].val, v4[v6].val)
                    v6 += 1
                    v7 -= 1
            for v8 in v4:
                if v8.left:
                    v1.append(v8.left)
                if v8.right:
                    v1.append(v8.right)
            v2 += 1
        return a1
