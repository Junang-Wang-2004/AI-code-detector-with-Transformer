class C1(object):

    def maxSumTrionic(self, a1):
        """
        """
        v1 = float('-inf')
        v2 = v3 = v4 = 0
        v5 = a1[0]
        for v6 in range(1, len(a1)):
            v5 += a1[v6]
            if a1[v6 - 1] > a1[v6]:
                if v6 - 2 >= 0 and a1[v6 - 2] < a1[v6 - 1]:
                    v3 = v6 - 1
                    while v2 < v4 or (a1[v2] < 0 and v2 + 1 < v3):
                        v5 -= a1[v2]
                        v2 += 1
            elif a1[v6 - 1] < a1[v6]:
                if v6 - 2 >= 0 and a1[v6 - 2] > a1[v6 - 1]:
                    v4 = v6 - 1
                if v2 != v3:
                    v1 = max(v1, v5)
            else:
                v2 = v3 = v4 = v6
                v5 = a1[v6]
        return v1
