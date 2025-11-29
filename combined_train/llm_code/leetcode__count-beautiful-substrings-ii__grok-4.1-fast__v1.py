class C1(object):

    def beautifulSubstrings(self, a1, a2):
        v1 = set('aeiou')
        v2 = len(a1)
        v3 = [0] * (v2 + 1)
        for v4 in range(v2):
            v3[v4 + 1] = v3[v4] + (1 if a1[v4] in v1 else -1)
        v5 = 1
        v6 = a2
        v7 = 2
        while v7 * v7 <= v6:
            v8 = 0
            while v6 % v7 == 0:
                v6 //= v7
                v8 += 1
            if v8 > 0:
                v9 = (v8 + 1) // 2 + (1 if v7 == 2 else 0)
                v5 *= v7 ** v9
            v7 += 1
        if v6 > 1:
            v9 = 1 + (1 if v6 == 2 else 0)
            v5 *= v6 ** v9
        v10 = {}
        v11 = 0
        for v12 in range(v2 + 1):
            v13 = v3[v12]
            v14 = v12 % v5
            v15 = (v13, v14)
            v11 += v10.get(v15, 0)
            v10[v15] = v10.get(v15, 0) + 1
        return v11
