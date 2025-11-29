class C1:

    def numberOfSpecialChars(self, a1):
        v1 = set()
        v2 = set()
        for v3 in a1:
            if v3.islower():
                v1.add(v3)
            elif v3.isupper():
                v2.add(v3.lower())
        return len(v1.intersection(v2))
