class C1:

    def matchReplacement(self, a1, a2, a3):
        v1 = {}
        for v2, v3 in a3:
            if v2 not in v1:
                v1[v2] = set()
            v1[v2].add(v3)
        v4, v5 = (len(a1), len(a2))
        for v6 in range(v4 - v5 + 1):
            v7 = False
            for v8 in range(v5):
                v9 = a2[v8]
                v10 = a1[v6 + v8]
                if v9 != v10 and v10 not in v1.get(v9, set()):
                    v7 = True
                    break
            if not v7:
                return True
        return False
