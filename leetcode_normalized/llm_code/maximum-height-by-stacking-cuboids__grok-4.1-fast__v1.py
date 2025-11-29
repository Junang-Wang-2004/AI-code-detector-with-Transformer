class C1(object):

    def maxHeight(self, a1):
        v1 = [sorted(box) for v2 in a1]
        v1.append([0] * 3)
        v1.sort()
        v3 = len(v1)
        v4 = [0] * v3
        for v5 in range(1, v3):
            for v6 in range(v5):
                if v1[v6][0] <= v1[v5][0] and v1[v6][1] <= v1[v5][1] and (v1[v6][2] <= v1[v5][2]):
                    v4[v5] = max(v4[v5], v4[v6] + v1[v5][2])
        return max(v4)
