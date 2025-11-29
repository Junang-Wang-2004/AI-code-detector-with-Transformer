class C1:

    def isSubstringPresent(self, a1):
        v1 = set()
        v2 = len(a1)
        for v3 in range(v2 - 1):
            v4 = a1[v3]
            v5 = a1[v3 + 1]
            if v4 == v5 or (v5, v4) in v1:
                return True
            v1.add((v4, v5))
        return False
