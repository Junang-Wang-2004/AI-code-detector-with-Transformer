class C1(object):

    def longestSubarray(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = False
        v6 = 0
        while v6 < v1:
            v7 = v6
            while v6 < v1 and a1[v6] == 0:
                v6 += 1
            v8 = v6 - v7
            if v8 > 0:
                v5 = True
            if v6 == v1:
                break
            v9 = v6
            while v6 < v1 and a1[v6] == 1:
                v6 += 1
            v10 = v6 - v9
            v2 = max(v2, v10)
            if v4 > 0 and v8 == 1:
                v3 = max(v3, v4 + v10)
            v4 = v10
        if not v5:
            return v2 - 1
        return max(v2, v3)
