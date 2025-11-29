from collections import deque

class C1:

    def correctBinaryTree(self, a1):
        v1 = deque([(a1, None)])
        while v1:
            v2 = len(v1)
            v3 = []
            for v4 in range(v2):
                v5, v6 = v1.popleft()
                v3.append((v5, v6))
            v7 = {nd for v8, v4 in v3}
            for v5, v6 in v3:
                if v5.right in v7:
                    if v6.left == v5:
                        v6.left = None
                    else:
                        v6.right = None
                    return a1
                if v5.left:
                    v1.append((v5.left, v5))
                if v5.right:
                    v1.append((v5.right, v5))
