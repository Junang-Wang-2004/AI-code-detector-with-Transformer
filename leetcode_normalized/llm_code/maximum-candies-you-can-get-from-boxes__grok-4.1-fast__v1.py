from collections import deque

class C1(object):

    def maxCandies(self, a1, a2, a3, a4, a5):
        v1 = set(a5)
        v2 = set()
        v3 = deque((b for v4 in a5 if a1[v4]))
        v5 = 0
        while v3:
            v6 = v3.popleft()
            if v6 in v2:
                continue
            v2.add(v6)
            v5 += a2[v6]
            for v7 in a3[v6]:
                a1[v7] = 1
                if v7 in v1 and v7 not in v2:
                    v3.append(v7)
            for v4 in a4[v6]:
                v1.add(v4)
                if a1[v4] and v4 not in v2:
                    v3.append(v4)
        return v5
