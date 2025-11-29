class C1(object):

    def maximalNetworkRank(self, a1, a2):
        """
        """
        v1 = 100
        v2 = v1 - 1

        def counting_sort(a1, a2=lambda x: x, a3=False):
            v1 = [0] * (v2 + 1)
            for v2 in a1:
                v1[a2(v2)] += 1
            for v3 in range(1, len(v1)):
                v1[v3] += v1[v3 - 1]
            v4 = [0] * len(a1)
            if not a3:
                for v2 in reversed(a1):
                    v1[a2(v2)] -= 1
                    v4[v1[a2(v2)]] = v2
            else:
                for v2 in a1:
                    v1[a2(v2)] -= 1
                    v4[v1[a2(v2)]] = v2
                v4.reverse()
            return v4
        v3 = [0] * a1
        v4 = collections.defaultdict(set)
        for v5, v6 in a2:
            v3[v5] += 1
            v3[v6] += 1
            v4[v5].add(v6)
            v4[v6].add(v5)
        v7 = counting_sort(range(a1), key=lambda x: v3[x], reverse=True)
        v8 = 2
        while v8 < a1:
            if v3[v7[v8]] != v3[v7[1]]:
                break
            v8 += 1
        v9 = v3[v7[0]] + v3[v7[1]] - 1
        for v10 in range(v8 - 1):
            for v11 in range(v10 + 1, v8):
                if v3[v7[v10]] + v3[v7[v11]] - int(v7[v10] in v4 and v7[v11] in v4[v7[v10]]) > v9:
                    return v3[v7[v10]] + v3[v7[v11]] - int(v7[v10] in v4 and v7[v11] in v4[v7[v10]])
        return v9
