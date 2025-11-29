class C1(object):

    def totalNumbers(self, a1):
        """
        """
        v1 = [0] * 10
        for v2 in a1:
            v1[v2] += 1
        v3 = sum((v1[i] != 0 for v4 in range(0, len(v1), 2)))
        v5 = sum((v1[v4] != 0 for v4 in range(1, len(v1), 2)))
        v6 = 0
        for v4 in range(2, len(v1), 2):
            if v1[v4] >= 3:
                v6 += 1
        v6 += v3 * (v5 + v3 - 1) * (v5 + v3 - 2)
        if v1[0]:
            v6 -= 1 * (v3 - 1) * (v5 + v3 - 2)
        for v4 in range(len(v1)):
            if v1[v4] < 2:
                continue
            if v4 == 0:
                v6 += v5 + v3 - 1
            elif v4 % 2:
                v6 += v3
            else:
                v6 += 3 * (v3 - 1) - int(v1[0] != 0)
                v6 += 2 * v5
        return v6
