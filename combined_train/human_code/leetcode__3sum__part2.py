class C1(object):

    def threeSum(self, a1):
        """
        """
        a1, v2, v3 = (sorted(a1), [], 0)
        while v3 < len(a1) - 2:
            if v3 == 0 or a1[v3] != a1[v3 - 1]:
                v4, v5 = (v3 + 1, len(a1) - 1)
                while v4 < v5:
                    if a1[v3] + a1[v4] + a1[v5] < 0:
                        v4 += 1
                    elif a1[v3] + a1[v4] + a1[v5] > 0:
                        v5 -= 1
                    else:
                        v2.append([a1[v3], a1[v4], a1[v5]])
                        v4, v5 = (v4 + 1, v5 - 1)
                        while v4 < v5 and a1[v4] == a1[v4 - 1]:
                            v4 += 1
                        while v4 < v5 and a1[v5] == a1[v5 + 1]:
                            v5 -= 1
            v3 += 1
        return v2
