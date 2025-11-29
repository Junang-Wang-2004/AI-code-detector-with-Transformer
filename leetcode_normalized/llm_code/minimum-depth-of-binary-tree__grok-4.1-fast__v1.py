class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def minDepth(self, a1):
        if not a1:
            return 0
        from collections import deque
        v1 = deque([(a1, 1)])
        while v1:
            v2, v3 = v1.popleft()
            if not v2.left and (not v2.right):
                return v3
            if v2.left:
                v1.append((v2.left, v3 + 1))
            if v2.right:
                v1.append((v2.right, v3 + 1))
