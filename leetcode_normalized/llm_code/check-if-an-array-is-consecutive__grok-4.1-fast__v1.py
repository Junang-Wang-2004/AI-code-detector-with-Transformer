class C1:

    def isConsecutive(self, a1):
        v1 = set(a1)
        if len(v1) != len(a1):
            return False
        v2 = min(v1)
        v3 = len(a1)
        return all((v2 + i in v1 for v4 in range(v3)))
