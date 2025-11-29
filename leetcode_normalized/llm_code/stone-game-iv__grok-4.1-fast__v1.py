class C1:

    def winnerSquareGame(self, a1):
        v1 = [False] * (a1 + 1)
        v2 = int(a1 ** 0.5) + 1
        for v3 in range(1, v2 + 1):
            v4 = v3 * v3
            for v5 in range(v4, a1 + 1):
                if not v1[v5 - v4]:
                    v1[v5] = True
        return v1[a1]
