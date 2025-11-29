class C1:

    def combinationSum2(self, a1, a2):
        a1.sort()
        v1 = []

        def backtrack(a1, a2, a3):
            if a3 == 0:
                v1.append(a2[:])
                return
            for v1 in range(a1, len(a1)):
                if v1 > a1 and a1[v1] == a1[v1 - 1]:
                    continue
                if a1[v1] > a3:
                    break
                a2.append(a1[v1])
                backtrack(v1 + 1, a2, a3 - a1[v1])
                a2.pop()
        backtrack(0, [], a2)
        return v1
