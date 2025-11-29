class C1:

    def subsetsWithDup(self, a1):
        a1.sort()
        v1 = []

        def backtrack(a1, a2):
            v1.append(a2[:])
            for v1 in range(a1, len(a1)):
                if v1 > a1 and a1[v1] == a1[v1 - 1]:
                    continue
                a2.append(a1[v1])
                backtrack(v1 + 1, a2)
                a2.pop()
        backtrack(0, [])
        return v1
