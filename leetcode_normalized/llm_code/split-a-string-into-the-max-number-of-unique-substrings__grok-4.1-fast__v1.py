class C1:

    def maxUniqueSplit(self, a1):
        v1 = len(a1)
        v2 = 1

        def backtrack(a1, a2, a3):
            nonlocal ans
            if a1 == v1:
                v1 = max(v1, a3)
                return
            if a3 + v1 - a1 <= v1:
                return
            for v2 in range(a1 + 1, v1 + 1):
                v3 = a1[a1:v2]
                if v3 not in a2:
                    a2.add(v3)
                    backtrack(v2, a2, a3 + 1)
                    a2.remove(v3)
        backtrack(0, set(), 0)
        return v2
