class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def levelOrderBottom(self, a1):
        if not a1:
            return []
        from collections import deque
        v1 = deque([a1])
        v2 = []
        while v1:
            v3 = len(v1)
            v4 = []
            for v5 in range(v3):
                v6 = v1.popleft()
                v4.append(v6.val)
                if v6.left:
                    v1.append(v6.left)
                if v6.right:
                    v1.append(v6.right)
            v2.append(v4)
        v2.reverse()
        return v2
