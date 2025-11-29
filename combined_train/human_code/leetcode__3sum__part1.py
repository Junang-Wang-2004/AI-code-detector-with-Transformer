class C1(object):

    def threeSum(self, a1):
        """
        """
        v1 = []
        a1.sort()
        for v2 in reversed(range(2, len(a1))):
            if v2 + 1 < len(a1) and a1[v2] == a1[v2 + 1]:
                continue
            v3 = -a1[v2]
            v4, v5 = (0, v2 - 1)
            while v4 < v5:
                if a1[v4] + a1[v5] < v3:
                    v4 += 1
                elif a1[v4] + a1[v5] > v3:
                    v5 -= 1
                else:
                    v1.append([a1[v4], a1[v5], a1[v2]])
                    v4 += 1
                    v5 -= 1
                    while v4 < v5 and a1[v4] == a1[v4 - 1]:
                        v4 += 1
                    while v4 < v5 and a1[v5] == a1[v5 + 1]:
                        v5 -= 1
        return v1
