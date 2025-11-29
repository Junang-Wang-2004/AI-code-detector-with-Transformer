class C1:

    def subsets(self, a1):
        a1.sort()
        v1 = []

        def backtrack(a1, a2):
            v1.append(list(a2))
            for v1 in range(a1, len(a1)):
                a2.append(a1[v1])
                backtrack(v1 + 1, a2)
                a2.pop()
        backtrack(0, [])
        return v1
