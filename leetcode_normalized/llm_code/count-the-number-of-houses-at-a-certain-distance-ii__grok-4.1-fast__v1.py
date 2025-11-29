class C1:

    def countOfPairs(self, a1: int, a2: int, a3: int) -> list[int]:
        v1, v2 = (a2 - 1, a3 - 1)
        if v1 > v2:
            v1, v2 = (v2, v1)
        v3 = [0] * a1
        for v4 in range(a1):
            v3[0] += 2
            v5 = min(abs(v4 - v1), abs(v4 - v2) + 1)
            v3[v5] += 1
            py
