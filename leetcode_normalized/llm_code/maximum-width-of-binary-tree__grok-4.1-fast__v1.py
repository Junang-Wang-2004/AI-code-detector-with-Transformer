from collections import deque

class C1:

    def widthOfBinaryTree(self, a1):
        if not a1:
            return 0
        v1 = deque([(a1, 0)])
        v2 = 0
        while v1:
            v3 = len(v1)
            v4 = float('inf')
            v5 = float('-inf')
            for v6 in range(v3):
                v7, v8 = v1.popleft()
                v4 = min(v4, v8)
                v5 = max(v5, v8)
                if v7.left:
                    v1.append((v7.left, v8 * 2))
                if v7.right:
                    v1.append((v7.right, v8 * 2 + 1))
            v2 = max(v2, v5 - v4 + 1)
        return v2
