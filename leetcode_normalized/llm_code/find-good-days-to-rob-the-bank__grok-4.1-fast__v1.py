class C1(object):

    def goodDaysToRobBank(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        for v3 in range(1, v1):
            v2[v3] = v2[v3 - 1] + 1 if a1[v3 - 1] >= a1[v3] else 0
        v4 = [0] * v1
        for v3 in range(v1 - 2, -1, -1):
            v4[v3] = v4[v3 + 1] + 1 if a1[v3] <= a1[v3 + 1] else 0
        v5 = []
        for v3 in range(v1):
            if v2[v3] >= a2 and v4[v3] >= a2:
                v5.append(v3)
        return v5
