class C1:

    def lastVisitedIntegers(self, a1):
        v1 = []
        v2 = -1
        v3 = []
        for v4 in a1:
            if v4 == 'prev':
                if v2 >= 0:
                    v3.append(v1[v2])
                else:
                    v3.append(-1)
                v2 -= 1
            else:
                v1.append(int(v4))
                v2 = len(v1) - 1
        return v3
