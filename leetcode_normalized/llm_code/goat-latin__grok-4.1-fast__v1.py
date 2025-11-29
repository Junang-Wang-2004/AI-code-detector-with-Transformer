class C1:

    def toGoatLatin(self, a1):
        v1 = a1.split()
        v2 = []
        for v3, v4 in enumerate(v1, start=1):
            if v4[0] not in 'aeiouAEIOU':
                v4 = v4[1:] + v4[0]
            v2.append(v4 + 'ma' + 'a' * v3)
        return ' '.join(v2)
