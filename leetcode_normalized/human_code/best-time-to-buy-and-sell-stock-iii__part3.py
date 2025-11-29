class C1(object):

    def maxProfit(self, a1):
        v1, v2, v3 = (float('inf'), 0, [])
        for v4 in a1:
            v1 = min(v1, v4)
            v2 = max(v2, v4 - v1)
            v3.append(v2)
        v5, v6, v7 = (0, 0, [])
        for v8 in reversed(list(range(len(a1)))):
            v5 = max(v5, a1[v8])
            v6 = max(v6, v5 - a1[v8])
            v7.insert(0, v6)
        v9 = 0
        for v8 in range(len(a1)):
            v9 = max(v9, v3[v8] + v7[v8])
        return v9
