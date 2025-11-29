class C1:

    def countConsistentStrings(self, a1, a2):
        v1 = set(a1)
        v2 = 0
        for v3 in a2:
            v4 = True
            for v5 in v3:
                if v5 not in v1:
                    v4 = False
                    break
            if v4:
                v2 += 1
        return v2
