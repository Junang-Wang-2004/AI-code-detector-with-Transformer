from collections import Counter

class C1:

    def permuteUnique(self, a1):
        v1 = Counter(a1)
        v2 = len(a1)
        v3 = []
        v4 = []

        def backtrack():
            if len(v4) == v2:
                v3.append(list(v4))
                return
            for v1 in v1:
                if v1[v1] > 0:
                    v1[v1] -= 1
                    v4.append(v1)
                    backtrack()
                    v4.pop()
                    v1[v1] += 1
        backtrack()
        return v3
