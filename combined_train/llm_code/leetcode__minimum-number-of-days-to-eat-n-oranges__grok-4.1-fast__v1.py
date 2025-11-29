from collections import deque

class C1:

    def minDays(self, a1):
        if a1 == 0:
            return 0
        v1 = {}
        v2 = deque([a1])
        v1[a1] = 0
        while v2:
            v3 = v2.popleft()
            if v3 == 0:
                return v1[v3]
            v4 = v3 - 1
            if v4 >= 0 and v4 not in v1:
                v1[v4] = v1[v3] + 1
                v2.append(v4)
            if v3 % 2 == 0:
                v5 = v3 // 2
                if v5 not in v1:
                    v1[v5] = v1[v3] + 1
                    v2.append(v5)
            if v3 % 3 == 0:
                v6 = v3 // 3
                if v6 not in v1:
                    v1[v6] = v1[v3] + 1
                    v2.append(v6)
