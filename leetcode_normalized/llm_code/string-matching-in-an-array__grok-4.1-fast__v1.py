class C1:

    def stringMatching(self, a1):
        v1 = len(a1)
        v2 = set()
        for v3 in range(v1):
            for v4 in range(v1):
                if v3 != v4 and a1[v3] in a1[v4]:
                    v2.add(v3)
                    break
        return [a1[v3] for v3 in range(v1) if v3 in v2]
