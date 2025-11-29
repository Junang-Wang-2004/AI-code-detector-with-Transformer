from collections import deque

class C1:

    def racecar(self, a1):
        v1 = deque([(0, 1, 0)])
        v2 = {(0, 1)}
        while v1:
            v3, v4, v5 = v1.popleft()
            if v3 == a1:
                return v5
            for v6, v7 in [(v4, v4 * 2), (0, -v4)]:
                v8 = v3 + v6
                v9 = (v8, v7)
                if v9 not in v2 and abs(v8) <= a1 * 2:
                    v2.add(v9)
                    v1.append((v8, v7, v5 + 1))
