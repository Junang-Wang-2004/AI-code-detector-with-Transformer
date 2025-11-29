class C1(object):

    def findTheLongestBalancedSubstring(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = -1
        while v3 < v1:
            v6 = v3
            while v3 < v1 and a1[v3] == a1[v6]:
                v3 += 1
            v7 = v3 - v6
            v8 = int(a1[v6])
            if v5 == 0 and v8 == 1:
                v2 = max(v2, 2 * min(v4, v7))
            v4 = v7
            v5 = v8
        return v2
