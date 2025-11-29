class C1:

    def isIsomorphic(self, a1, a2):
        if len(a1) != len(a2):
            return False

        def pattern(a1):
            v1 = {}
            v2 = []
            for v3, v4 in enumerate(a1):
                if v4 not in v1:
                    v1[v4] = v3
                v2.append(v1[v4])
            return v2
        return pattern(a1) == pattern(a2)
