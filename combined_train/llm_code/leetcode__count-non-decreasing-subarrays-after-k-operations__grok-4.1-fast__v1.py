from collections import deque

class C1:

    def countNonDecreasingSubarrays(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = deque()
        v5 = v1 - 1
        for v6 in range(v1 - 1, -1, -1):
            while v4 and a1[v4[-1]] < a1[v6]:
                v7 = v4.pop()
                v8 = v4[-1] - 1 if v4 else v5
                v3 += (v8 - v7 + 1) * (a1[v6] - a1[v7])
            v4.append(v6)
            while v3 > a2:
                v3 -= a1[v4[0]] - a1[v5]
                if v4[0] == v5:
                    v4.popleft()
                v5 -= 1
            v2 += v5 - v6 + 1
        return v2
