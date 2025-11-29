class C1:

    def generatePossibleNextMoves(self, a1):
        v1 = []
        v2 = list(a1)
        v3 = len(v2)
        for v4 in range(v3 - 1):
            if v2[v4] == '+' and v2[v4 + 1] == '+':
                v5 = v2[:]
                v5[v4] = '-'
                v5[v4 + 1] = '-'
                v1.append(''.join(v5))
        return v1
