from collections import deque

class C1:

    def kthLargestLevelSum(self, a1, a2):
        v1 = []
        if not a1:
            v2 = 0
        else:
            v3 = deque([a1])
            while v3:
                v4 = 0
                v5 = len(v3)
                for v6 in range(v5):
                    v7 = v3.popleft()
                    v4 += v7.val
                    if v7.left:
                        v3.append(v7.left)
                    if v7.right:
                        v3.append(v7.right)
                v1.append(v4)
            v2 = len(v1)
        if v2 < a2:
            return -1
        v1.sort(reverse=True)
        return v1[a2 - 1]
