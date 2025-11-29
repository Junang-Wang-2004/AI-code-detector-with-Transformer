class C1:

    def reorderSpaces(self, a1):
        v1 = a1.split()
        v2 = len(a1) - sum((len(w) for v3 in v1))
        v4 = len(v1)
        v5 = v2 // (v4 - 1) if v4 > 1 else 0
        v6 = v2 - v5 * max(v4 - 1, 0)
        v7 = ' ' * v5
        return v7.join(v1) + ' ' * v6
