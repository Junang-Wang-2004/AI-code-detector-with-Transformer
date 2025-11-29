class C1(object):

    def countOfPairs(self, a1, a2, a3):
        """
        """
        a2, a3 = (a2 - 1, a3 - 1)
        if a2 > a3:
            a2, a3 = (a3, a2)
        v3 = [0] * a1
        for v4 in range(a1):
            v3[0] += 1 + 1
            v3[min(abs(v4 - a2), abs(v4 - a3) + 1)] += 1
            v3[min(abs(v4 - a3), abs(v4 - a2) + 1)] += 1
            v3[min(abs(v4 - 0), abs(v4 - a3) + 1 + abs(a2 - 0))] -= 1
            v3[min(abs(v4 - (a1 - 1)), abs(v4 - a2) + 1 + abs(a3 - (a1 - 1)))] -= 1
            v3[max(a2 - v4, 0) + max(v4 - a3, 0) + (a3 - a2 + 0) // 2] -= 1
            v3[max(a2 - v4, 0) + max(v4 - a3, 0) + (a3 - a2 + 1) // 2] -= 1
        for v4 in range(a1 - 1):
            v3[v4 + 1] += v3[v4]
        return v3
