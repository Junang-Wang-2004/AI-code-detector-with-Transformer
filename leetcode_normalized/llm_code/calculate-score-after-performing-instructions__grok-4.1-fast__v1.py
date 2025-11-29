class C1:

    def calculateScore(self, a1, a2):
        v1 = 0
        v2 = set()
        v3 = 0
        v4 = len(a1)
        while 0 <= v3 < v4 and v3 not in v2:
            v2.add(v3)
            if a1[v3] == 'add':
                v1 += a2[v3]
                v3 += 1
            else:
                v3 += a2[v3]
        return v1
