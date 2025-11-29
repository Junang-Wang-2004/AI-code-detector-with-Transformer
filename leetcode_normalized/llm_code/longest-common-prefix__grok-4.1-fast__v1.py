class C1:

    def longestCommonPrefix(self, a1):
        if not a1:
            return ''
        a1.sort()
        v1, v2 = (a1[0], a1[-1])
        v3 = 0
        v4 = min(len(v1), len(v2))
        while v3 < v4 and v1[v3] == v2[v3]:
            v3 += 1
        return v1[:v3]
