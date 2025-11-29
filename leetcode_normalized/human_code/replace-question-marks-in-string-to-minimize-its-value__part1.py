class C1(object):

    def minimizeStringValue(self, a1):
        """
        """

        def counting_sort(a1):
            for v1 in range(len(a1)):
                for v2 in range(a1[v1]):
                    yield v1

        def fill(a1):
            v1 = [0] * 26
            v2 = [(x, i) for v3, v4 in enumerate(a1)]
            v2.sort()
            v5 = a1.count('?')
            v6 = 0
            for v3 in range(len(v2) - 1):
                if v6 + (v2[v3 + 1][0] - v2[v3][0]) * (v3 + 1) > v5:
                    break
                v6 += (v2[v3 + 1][0] - v2[v3][0]) * (v3 + 1)
            else:
                v3 = len(v2) - 1
            v7, v8 = divmod(v5 - v6, v3 + 1)
            for v9 in range(v3 + 1):
                v1[v2[v9][1]] = v2[v3][0] - v2[v9][0] + v7
            v10 = [0] * 26
            for v9 in range(v3 + 1):
                v10[v2[v9][1]] += 1
            v11 = counting_sort(v10)
            for v12 in range(v8):
                v1[next(v11)] += 1
            return v1
        v1 = [0] * 26
        for v2 in a1:
            if v2 == '?':
                continue
            v1[ord(v2) - ord('a')] += 1
        v3 = counting_sort(fill(v1))
        v4 = list(a1)
        for v5 in range(len(v4)):
            if v4[v5] != '?':
                continue
            v4[v5] = chr(ord('a') + next(v3))
        return ''.join(v4)
