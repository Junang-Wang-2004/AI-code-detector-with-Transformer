class C1(object):

    def numDecodings(self, a1):
        v1 = len(a1)
        if v1 == 0 or a1[0] == '0':
            return 0
        v2 = 1
        v3 = 1
        for v4 in range(1, v1):
            v5 = 0
            if a1[v4] != '0':
                v5 = v3
            v6 = a1[v4 - 1:v4 + 1]
            if 10 <= int(v6) <= 26:
                v5 += v2
            v2 = v3
            v3 = v5
        return v3
