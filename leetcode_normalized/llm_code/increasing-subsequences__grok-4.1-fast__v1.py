class C1:

    def findSubsequences(self, a1):
        v1 = []

        def explore(a1, a2):
            if len(a2) >= 2:
                v1.append(a2)
            v1 = set()
            for v2 in range(a1, len(a1)):
                if not a2 or a1[v2] >= a2[-1]:
                    if a1[v2] not in v1:
                        v1.add(a1[v2])
                        explore(v2 + 1, a2 + [a1[v2]])
        explore(0, [])
        return v1
