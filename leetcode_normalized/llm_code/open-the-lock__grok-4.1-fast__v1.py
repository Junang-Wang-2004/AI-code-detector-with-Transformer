from collections import deque

class C1:

    def openLock(self, a1, a2):
        v1 = set(a1)
        v2 = set(v1)
        if '0000' in v2:
            return -1
        v3 = deque([('0000', 0)])
        v2.add('0000')
        while v3:
            v4, v5 = v3.popleft()
            if v4 == a2:
                return v5
            for v6 in range(4):
                v7 = int(v4[v6])
                for v8 in (-1, 1):
                    v9 = (v7 + v8) % 10
                    v10 = v4[:v6] + str(v9) + v4[v6 + 1:]
                    if v10 not in v2:
                        v2.add(v10)
                        v3.append((v10, v5 + 1))
        return -1
