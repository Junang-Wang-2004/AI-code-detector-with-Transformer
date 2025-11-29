class C1:

    def mostCommonWord(self, a1, a2):
        v1 = set(a2)
        v2 = {}
        for v3 in a1.lower().split():
            v4 = ''.join((character for v5 in v3 if v5.isalpha()))
            if v4 and v4 not in v1:
                v2[v4] = v2.get(v4, 0) + 1
        return max(v2, key=v2.get)
