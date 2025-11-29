class C1(object):

    def countOfSubstrings(self, a1, a2):
        """
        """
        v1 = set('aeiou')

        def update(a1, a2):
            if a1[a1] not in v1:
                curr2[0] += a2
                return
            v1 = ord(a1[a1]) - ord('a')
            if cnt1[v1] == 0:
                curr1[0] += 1
            cnt1[v1] += a2
            if cnt1[v1] == 0:
                curr1[0] -= 1
        v2 = 0
        v3, v4 = ([0] * 26, [0] * 26)
        v5, v6 = ([0], [0])
        v7 = v8 = 0
        for v9 in range(len(a1)):
            update(v9, +1)
            while v6[0] > a2:
                update(v8, -1)
                if v8 < v7:
                    assert a1[v8] in v1
                    v4[ord(a1[v8]) - ord('a')] -= 1
                v8 += 1
                v7 = max(v7, v8)
            if not (v5[0] == len(v1) and v6[0] == a2):
                continue
            while a1[v7] in v1 and v3[ord(a1[v7]) - ord('a')] - (v4[ord(a1[v7]) - ord('a')] + 1) >= 1:
                v4[ord(a1[v7]) - ord('a')] += 1
                v7 += 1
            v2 += v7 - v8 + 1
        return v2
