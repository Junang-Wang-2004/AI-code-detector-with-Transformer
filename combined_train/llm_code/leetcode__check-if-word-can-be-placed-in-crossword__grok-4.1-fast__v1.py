class C1:

    def placeWordInCrossword(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = a2[::-1]

        def fits(a1, a2):
            return len(a1) == len(a2) and all((a1[k] == ' ' or a1[k] == a2[k] for v1 in range(len(a1))))
        for v4 in range(v1):
            v5 = []
            for v6 in range(v2):
                v7 = a1[v4][v6]
                if v7 == '#':
                    if fits(v5, a2) or fits(v5, v3):
                        return True
                    v5 = []
                else:
                    v5.append(v7)
            if fits(v5, a2) or fits(v5, v3):
                return True
        for v6 in range(v2):
            v5 = []
            for v4 in range(v1):
                v7 = a1[v4][v6]
                if v7 == '#':
                    if fits(v5, a2) or fits(v5, v3):
                        return True
                    v5 = []
                else:
                    v5.append(v7)
            if fits(v5, a2) or fits(v5, v3):
                return True
        return False
