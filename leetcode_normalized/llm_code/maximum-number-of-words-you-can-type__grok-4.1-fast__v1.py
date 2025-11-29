class C1:

    def canBeTypedWords(self, a1, a2):
        v1 = set(a2)
        v2 = 0
        for v3 in a1.split():
            if all((char not in v1 for v4 in v3)):
                v2 += 1
        return v2
