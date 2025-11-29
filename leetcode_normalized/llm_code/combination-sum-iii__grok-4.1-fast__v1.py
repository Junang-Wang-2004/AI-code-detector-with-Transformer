class C1:

    def combinationSum3(self, a1, a2):
        v1 = []

        def backtrack(a1, a2, a3):
            if len(a1) == a1:
                if a2 == a2:
                    v1.append(a1[:])
                return
            for v1 in range(a3, 10):
                if a2 + v1 > a2:
                    break
                a1.append(v1)
                backtrack(a1, a2 + v1, v1 + 1)
                a1.pop()
        backtrack([], 0, 1)
        return v1
