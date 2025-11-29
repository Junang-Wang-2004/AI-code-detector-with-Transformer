class C1(object):

    def minimizeStringValue(self, a1):
        """
        """

        def counting_sort(a1):
            for v1 in range(len(a1)):
                for v2 in range(a1[v1]):
                    yield v1
        v1 = [0] * 26
        for v2 in a1:
            if v2 == '?':
                continue
            v1[ord(v2) - ord('a')] += 1
        v3 = [0] * 26
        for v4 in range(a1.count('?')):
            v5 = min(range(len(v1)), key=lambda x: v1[v2] + v3[v2])
            v3[v5] += 1
        v6 = counting_sort(v3)
        v7 = list(a1)
        for v5 in range(len(v7)):
            if v7[v5] != '?':
                continue
            v7[v5] = chr(ord('a') + next(v6))
        return ''.join(v7)
