from collections import deque

class C1:

    def constrainedSubsetSum(self, a1, a2):
        v1 = float('-inf')
        v2 = deque()
        for v3 in range(len(a1)):
            while v2 and v2[0][0] < v3 - a2:
                v2.popleft()
            v4 = v2[0][1] if v2 else 0
            v5 = a1[v3] + v4
            while v2 and v2[-1][1] <= v5:
                v2.pop()
            if v5 > 0:
                v2.append((v3, v5))
            v1 = max(v1, v5)
        return v1
