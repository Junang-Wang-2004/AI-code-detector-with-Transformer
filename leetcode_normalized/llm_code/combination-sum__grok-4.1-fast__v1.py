class C1:

    def combinationSum(self, a1, a2):
        v1 = sorted(a1)
        v2 = []

        def backtrack(a1, a2, a3):
            if a3 == 0:
                v2.append(list(a2))
                return
            for v1 in range(a1, len(v1)):
                if v1[v1] > a3:
                    break
                a2.append(v1[v1])
                backtrack(v1, a2, a3 - v1[v1])
                a2.pop()
        backtrack(0, [], a2)
        return v2
