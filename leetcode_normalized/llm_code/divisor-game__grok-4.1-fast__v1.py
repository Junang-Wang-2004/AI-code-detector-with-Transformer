class C1:

    def divisorGame(self, a1):
        v1 = [False] * (a1 + 1)
        for v2 in range(2, a1 + 1):
            v1[v2] = any((v2 % x == 0 and (not v1[v2 - x]) for v3 in range(1, v2)))
        return v1[a1]
