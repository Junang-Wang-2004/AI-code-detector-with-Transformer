from collections import deque

class C1:

    def minimumOperationsToMakeEqual(self, a1, a2):
        if a1 == a2:
            return 0
        if a2 > a1:
            return a2 - a1
        v1 = a1 + (a1 - a2)
        v2 = {a1: 0}
        v3 = deque([a1])
        while v3:
            v4 = v3.popleft()
            if v4 == a2:
                return v2[v4]
            for v5 in (v4 - 1, v4 + 1):
                if 0 <= v5 <= v1 and v5 not in v2:
                    v2[v5] = v2[v4] + 1
                    v3.append(v5)
            for v6 in (5, 11):
                if v4 % v6 == 0:
                    v5 = v4 // v6
                    if 0 <= v5 <= v1 and v5 not in v2:
                        v2[v5] = v2[v4] + 1
                        v3.append(v5)
        return -1
