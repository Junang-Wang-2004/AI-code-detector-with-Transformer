from collections import deque

class C1(object):

    def averageOfLevels(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = deque([a1])
        while v2:
            v3 = len(v2)
            v4 = 0
            for v5 in range(v3):
                v6 = v2.popleft()
                v4 += v6.val
                if v6.left:
                    v2.append(v6.left)
                if v6.right:
                    v2.append(v6.right)
            v1.append(v4 / v3)
        return v1
