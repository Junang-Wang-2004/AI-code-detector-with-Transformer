from collections import deque

class C1:

    def largestValues(self, a1):
        if not a1:
            return []
        v1 = deque([a1])
        v2 = []
        while v1:
            v3 = float('-inf')
            v4 = len(v1)
            for v5 in range(v4):
                v6 = v1.popleft()
                v3 = max(v3, v6.val)
                if v6.left:
                    v1.append(v6.left)
                if v6.right:
                    v1.append(v6.right)
            v2.append(v3)
        return v2
