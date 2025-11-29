from sortedcontainers import SortedDict

class C1(object):

    def continuousSubarrays(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = SortedDict()
        for v4 in range(len(a1)):
            v3[a1[v4]] = v4
            v5 = []
            for v6, v7 in list(v3.items()):
                if a1[v4] - v6 <= 2:
                    break
                v2 = max(v2, v7 + 1)
                v5.append(v6)
            for v6, v7 in reversed(list(v3.items())):
                if v6 - a1[v4] <= 2:
                    break
                v2 = max(v2, v7 + 1)
                v5.append(v6)
            for v6 in v5:
                del v3[v6]
            v1 += v4 - v2 + 1
        return v1
