class C1:

    def countArrangement(self, a1):
        v1 = [False] * (a1 + 1)

        def backtrack(a1):
            if a1 > a1:
                return 1
            v1 = 0
            for v2 in range(1, a1 + 1):
                if not v1[v2] and (v2 % a1 == 0 or a1 % v2 == 0):
                    v1[v2] = True
                    v1 += backtrack(a1 + 1)
                    v1[v2] = False
            return v1
        return backtrack(1)
