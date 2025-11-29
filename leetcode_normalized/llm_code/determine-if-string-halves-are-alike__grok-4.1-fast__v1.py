class C1:

    def halvesAreAlike(self, a1):
        v1 = set('aeiouAEIOU')
        v2 = len(a1)
        v3 = v2 // 2
        v4 = sum((c in v1 for v5 in a1[:v3]))
        v6 = sum((v5 in v1 for v5 in a1[v3:]))
        return v4 == v6
