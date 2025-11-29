class C1(object):

    def substringXorQueries(self, a1, a2):
        if not a2:
            return []
        v1 = max((a ^ b for v2, v3 in a2))
        v4 = {}
        v5 = -1
        for v6, v7 in enumerate(a1):
            if v7 == '0' and v5 == -1:
                v5 = v6
        if v5 != -1:
            v4[0] = [v5, v5]
        for v8 in range(len(a1)):
            if a1[v8] != '1':
                continue
            v9 = 0
            for v10 in range(v8, len(a1)):
                v9 = v9 << 1 | int(a1[v10])
                if v9 > v1:
                    break
                if v9 not in v4:
                    v4[v9] = [v8, v10]
        v11 = []
        for v12, v13 in a2:
            v14 = v12 ^ v13
            v11.append(v4.get(v14, [-1, -1]))
        return v11
