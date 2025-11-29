class C1(object):

    def minNumberOfFrogs(self, a1):
        v1 = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        v2 = [0] * 5
        v3 = 0
        for v4 in a1:
            if v4 not in v1:
                return -1
            v5 = v1[v4]
            if v2[v5] == 0:
                if v5 != 0:
                    return -1
                v3 += 1
            else:
                v2[v5] -= 1
            v6 = (v5 + 1) % 5
            v2[v6] += 1
        for v7 in range(1, 5):
            if v2[v7] > 0:
                return -1
        return v3
