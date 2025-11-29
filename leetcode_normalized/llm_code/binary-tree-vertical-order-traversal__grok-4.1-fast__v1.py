from collections import deque

class C1:

    def verticalOrder(self, a1):
        if not a1:
            return []
        v1 = {}
        v2 = deque([(a1, 0)])
        while v2:
            v3, v4 = v2.popleft()
            v1.setdefault(v4, []).append(v3.val)
            if v3.left:
                v2.append((v3.left, v4 - 1))
            if v3.right:
                v2.append((v3.right, v4 + 1))
        v5 = sorted(v1)
        return [v1[c] for v6 in v5]
