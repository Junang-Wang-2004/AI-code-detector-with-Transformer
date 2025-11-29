import collections

class C1(object):

    def fourSum(self, a1, a2):
        """
        """
        a1.sort()
        v1 = []
        for v2 in range(len(a1) - 3):
            if v2 and a1[v2] == a1[v2 - 1]:
                continue
            for v3 in range(v2 + 1, len(a1) - 2):
                if v3 != v2 + 1 and a1[v3] == a1[v3 - 1]:
                    continue
                v4 = a2 - a1[v2] - a1[v3]
                v5, v6 = (v3 + 1, len(a1) - 1)
                while v5 < v6:
                    if a1[v5] + a1[v6] == v4:
                        v1.append([a1[v2], a1[v3], a1[v5], a1[v6]])
                        v6 -= 1
                        v5 += 1
                        while v5 < v6 and a1[v5] == a1[v5 - 1]:
                            v5 += 1
                        while v5 < v6 and a1[v6] == a1[v6 + 1]:
                            v6 -= 1
                    elif a1[v5] + a1[v6] > v4:
                        v6 -= 1
                    else:
                        v5 += 1
        return v1
