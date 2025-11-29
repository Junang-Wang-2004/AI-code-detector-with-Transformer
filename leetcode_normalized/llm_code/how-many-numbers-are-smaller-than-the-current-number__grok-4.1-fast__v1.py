class C1:

    def smallerNumbersThanCurrent(self, a1):
        v1 = [0] * 101
        for v2 in a1:
            v1[v2] += 1
        v3 = [0] * 101
        v3[0] = v1[0]
        for v4 in range(1, 101):
            v3[v4] = v3[v4 - 1] + v1[v4]
        v5 = []
        for v2 in a1:
            v5.append(v3[v2] - v1[v2])
        return v5
