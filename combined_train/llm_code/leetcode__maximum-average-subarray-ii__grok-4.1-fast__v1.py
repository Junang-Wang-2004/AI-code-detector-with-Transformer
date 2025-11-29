class C1(object):

    def findMaxAverage(self, a1, a2):
        v1 = min(a1)
        v2 = max(a1)
        for v3 in range(60):
            v4 = (v1 + v2) / 2
            v5 = [0.0]
            v6 = 0.0
            for v7 in a1:
                v6 += v7 - v4
                v5.append(v6)
            v8 = False
            v9 = 0.0
            for v10 in range(a2, len(v5)):
                if v10 - a2 > 0:
                    v9 = min(v9, v5[v10 - a2])
                if v5[v10] >= v9:
                    v8 = True
                    break
            if v8:
                v1 = v4
            else:
                v2 = v4
        return v1
