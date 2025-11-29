class C1(object):

    def minSubarraySort(self, a1, a2):
        v1 = len(a1)
        if a2 == 1:
            return [0] * v1

        def get_keeps(a1):
            v1 = [v1] * v1
            v2 = []
            for v3 in range(v1 - 1, -1, -1):
                while v2 and a1[v2[-1]] < a1[v3]:
                    v2.pop()
                if v2:
                    v1[v3] = v2[-1]
                v2.append(v3)
            v4 = []
            v5 = -1
            v6 = 0
            for v7 in range(1, v1):
                if a1[v7] < a1[v7 - 1]:
                    v5 = v7
                if v7 < a2 - 1:
                    continue
                v8 = max(v6, v7 - a2 + 1)
                while v8 < v1 and v1[v8] <= v5:
                    v8 = v1[v8]
                v9 = max(v7 - v1[v8] + 1, 0)
                v4.append(v9)
                v6 = v8
            return v4
        v2 = get_keeps(a1)
        v3 = [-a1[v1 - 1 - p] for v4 in range(v1)]
        v5 = get_keeps(v3)
        v6 = v1 - a2 + 1
        return [max(a2 - v5[v6 - 1 - i] - v2[i], 0) for v7 in range(v6)]
