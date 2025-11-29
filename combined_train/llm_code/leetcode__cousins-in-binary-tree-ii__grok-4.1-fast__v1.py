from collections import deque

class C1:

    def replaceValueInTree(self, a1):
        if not a1:
            return a1
        v1 = deque([(a1, a1.val)])
        while v1:
            v2 = sum((nd.val for v3, v4 in v1))
            v5 = deque()
            while v1:
                v3, v6 = v1.popleft()
                v3.val = v2 - v6
                v7 = 0
                if v3.left:
                    v7 += v3.left.val
                if v3.right:
                    v7 += v3.right.val
                if v3.left:
                    v5.append((v3.left, v7))
                if v3.right:
                    v5.append((v3.right, v7))
            v1 = v5
        return a1
