class C1:

    def numTilePossibilities(self, a1: str) -> int:
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - 65] += 1

        def explore(a1):
            v1 = 0
            for v2 in range(26):
                if a1[v2] > 0:
                    a1[v2] -= 1
                    v1 += 1 + explore(a1)
                    a1[v2] += 1
            return v1
        return explore(v1)
