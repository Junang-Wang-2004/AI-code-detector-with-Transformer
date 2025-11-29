class C1:

    def wordsTyping(self, a1: List[str], a2: int, a3: int) -> int:
        v1 = len(a1)
        v2 = [len(w) for v3 in a1]

        def fit_from(a1: int) -> int:
            if v2[a1] > a3:
                return 0
            v1 = a3 - v2[a1]
            v2 = 1
            v3 = (a1 + 1) % v1
            while v1 >= 1 + v2[v3]:
                v1 -= 1 + v2[v3]
                v2 += 1
                v3 = (v3 + 1) % v1
            return v2
        v4 = [fit_from(i) for v5 in range(v1)]
        v6 = 0
        v7 = 0
        for v8 in range(a2):
            v6 += v4[v7]
            v7 = (v7 + v4[v7]) % v1
        return v6 // v1
