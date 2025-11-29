class C1:

    def permute(self, a1):
        v1 = []

        def backtrack(a1):
            if a1 == len(a1):
                v1.append(a1[:])
                return
            for v1 in range(a1, len(a1)):
                a1[a1], a1[v1] = (a1[v1], a1[a1])
                backtrack(a1 + 1)
                a1[a1], a1[v1] = (a1[v1], a1[a1])
        backtrack(0)
        return v1
