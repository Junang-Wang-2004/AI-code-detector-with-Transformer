import collections

class C1(object):

    def maximalNetworkRank(self, a1, a2):
        """
        """
        v1 = [0] * a1
        v2 = collections.defaultdict(set)
        for v3, v4 in a2:
            v1[v3] += 1
            v1[v4] += 1
            v2[v3].add(v4)
            v2[v4].add(v3)
        v5 = list(range(a1))
        v5.sort(key=lambda x: -v1[x])
        v6 = 2
        while v6 < a1:
            if v1[v5[v6]] != v1[v5[1]]:
                break
            v6 += 1
        v7 = v1[v5[0]] + v1[v5[1]] - 1
        for v8 in range(v6 - 1):
            for v9 in range(v8 + 1, v6):
                if v1[v5[v8]] + v1[v5[v9]] - int(v5[v8] in v2 and v5[v9] in v2[v5[v8]]) > v7:
                    return v1[v5[v8]] + v1[v5[v9]] - int(v5[v8] in v2 and v5[v9] in v2[v5[v8]])
        return v7
