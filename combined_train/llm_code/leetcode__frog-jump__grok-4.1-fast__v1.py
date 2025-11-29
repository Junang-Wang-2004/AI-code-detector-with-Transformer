from collections import deque

class C1:

    def canCross(self, a1):
        if len(a1) < 2 or a1[1] != 1:
            return False
        v1 = a1[-1]
        v2 = set(a1)
        v3 = deque([(1, 1)])
        v4 = set([(1, 1)])
        while v3:
            v5, v6 = v3.popleft()
            if v5 == v1:
                return True
            for v7 in (-1, 0, 1):
                v8 = v6 + v7
                if v8 > 0:
                    v9 = v5 + v8
                    v10 = (v9, v8)
                    if v9 in v2 and v10 not in v4:
                        v4.add(v10)
                        v3.append(v10)
        return False
