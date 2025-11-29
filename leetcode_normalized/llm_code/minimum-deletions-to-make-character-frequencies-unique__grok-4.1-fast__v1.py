class C1(object):

    def minDeletions(self, a1):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = sorted((f for v4 in v1 if v4 > 0))[::-1]
        v5 = set()
        v6 = 0
        for v7 in v3:
            v8 = v7
            while v8 > 0 and v8 in v5:
                v8 -= 1
                v6 += 1
            if v8 > 0:
                v5.add(v8)
        return v6
