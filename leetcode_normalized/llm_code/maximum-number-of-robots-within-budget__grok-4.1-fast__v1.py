from collections import deque

class C1:

    def maximumRobots(self, a1, a2, a3):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = deque()
        for v6 in range(v1):
            while v5 and a1[v5[-1]] <= a1[v6]:
                v5.pop()
            v5.append(v6)
            v3 += a2[v6]
            while v4 <= v6 and a1[v5[0]] + (v6 - v4 + 1) * v3 > a3:
                v3 -= a2[v4]
                v4 += 1
                while v5 and v5[0] < v4:
                    v5.popleft()
            v2 = max(v2, v6 - v4 + 1)
        return v2
