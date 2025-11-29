class C1(object):

    def maxSubstringLength(self, a1):
        """
        """

        def update(a1, a2, a3, a4):
            a1 = ord(a1) - ord('a')
            if cnt2[a1] == cnt[a1]:
                a4 -= 1
            if cnt2[a1] == 0:
                a3 += 1
            cnt2[a1] += a2
            if cnt2[a1] == 0:
                a3 -= 1
            if cnt2[a1] == cnt[a1]:
                a4 += 1
            return (a3, a4)
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = -1
        for v4 in range(1, sum((v2 != 0 for v2 in v1))):
            v5 = [0] * 26
            v6 = v7 = v8 = 0
            for v9 in range(len(a1)):
                v7, v8 = update(a1[v9], +1, v7, v8)
                while v7 == v4 + 1:
                    v7, v8 = update(a1[v6], -1, v7, v8)
                    v6 += 1
                if v8 == v4:
                    v3 = max(v3, v9 - v6 + 1)
        return v3
