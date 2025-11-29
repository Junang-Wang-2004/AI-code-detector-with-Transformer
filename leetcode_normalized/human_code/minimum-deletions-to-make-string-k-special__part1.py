class C1(object):

    def minimumDeletions(self, a1, a2):
        """
        """

        def counting_sort(a1, a2=lambda x: x, a3=False):
            v1 = [0] * (max(a1, key=a2) + 1)
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
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = counting_sort([v2 for v2 in v1 if v2])
        v4 = float('inf')
        v5 = v6 = 0
        v7 = len(a1)
        v8 = -1
        for v9 in range(len(v3)):
            if v9 + 1 < len(v3) and v3[v9 + 1] == v3[v9]:
                continue
            while v5 < len(v3) and v3[v5] <= v3[v9] + a2:
                v7 -= v3[v5]
                v5 += 1
            v4 = min(v4, v6 + (v7 - (v3[v9] + a2) * (len(v3) - v5)))
            v6 += v3[v9] * (v9 - v8)
            v8 = v9
        return v4
