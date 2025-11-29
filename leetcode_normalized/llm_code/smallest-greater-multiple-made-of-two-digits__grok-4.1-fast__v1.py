from collections import deque

class C1:

    def findInteger(self, a1, a2, a3):
        v1 = (1 << 31) - 1
        v2 = sorted(set([a2, a3]))
        v3 = deque()
        for v4 in v2:
            v5 = v4
            if a1 < v5 <= v1 and v5 % a1 == 0:
                return v5
            v3.append(v5)
        v6 = set(v3)
        while v3:
            v7 = v3.popleft()
            for v4 in v2:
                v8 = v7 * 10 + v4
                if v8 > v1:
                    continue
                if v8 in v6:
                    continue
                v6.add(v8)
                if a1 < v8 and v8 % a1 == 0:
                    return v8
                v3.append(v8)
        return -1
