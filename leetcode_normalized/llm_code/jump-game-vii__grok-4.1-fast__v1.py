from collections import deque

class C1:

    def canReach(self, a1, a2, a3):
        v1 = len(a1)
        v2 = deque([0])
        for v3 in range(1, v1):
            while v2 and v2[0] < v3 - a3:
                v2.popleft()
            v4 = a1[v3] == '0' and v2 and (v2[0] <= v3 - a2)
            if v4:
                v2.append(v3)
        return bool(v2) and v2[-1] == v1 - 1
