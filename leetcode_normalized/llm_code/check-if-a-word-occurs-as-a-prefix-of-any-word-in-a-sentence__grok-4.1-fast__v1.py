class C1:

    def isPrefixOfWord(self, a1, a2):
        v1 = a1.split()
        for v2, v3 in enumerate(v1, start=1):
            if v3.startswith(a2):
                return v2
        return -1
