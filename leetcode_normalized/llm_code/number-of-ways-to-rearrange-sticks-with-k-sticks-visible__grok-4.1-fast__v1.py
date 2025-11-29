class C1:

    def rearrangeSticks(self, a1: int, a2: int) -> int:
        v1 = 10 ** 9 + 7
        v2 = [0] * (a2 + 1)
        v2[1] = 1
        for v3 in range(2, a1 + 1):
            v4 = v3 - 1
            for v5 in range(a2, 0, -1):
                v2[v5] = (v2[v5 - 1] + v4 * v2[v5]) % v1
        return v2[a2]
