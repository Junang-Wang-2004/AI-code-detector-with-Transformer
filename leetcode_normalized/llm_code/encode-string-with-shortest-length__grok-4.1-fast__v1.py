class C1(object):

    def encode(self, a1):
        v1 = len(a1)
        v2 = {}

        def helper(a1, a2):
            if a2 - a1 <= 1:
                return a1[a1:a2]
            v1 = (a1, a2)
            if v1 in v2:
                return v2[v1]
            v2 = a1[a1:a2]
            for v3 in range(a1 + 1, a2):
                v4 = helper(a1, v3)
                v5 = helper(v3, a2)
                v6 = v4 + v5
                if len(v6) < len(v2):
                    v2 = v6
            v7 = a2 - a1
            if v7 > 1:
                v8 = [0] * v7
                v9 = 0
                for v10 in range(1, v7):
                    while v9 > 0 and a1[a1 + v10] != a1[a1 + v9]:
                        v9 = v8[v9 - 1]
                    if a1[a1 + v10] == a1[a1 + v9]:
                        v9 += 1
                    v8[v10] = v9
                v11 = v7 - v8[v7 - 1]
                if v11 < v7 and v7 % v11 == 0:
                    v12 = helper(a1, a1 + v11)
                    v13 = v7 // v11
                    v14 = f'{v13}[{v12}]'
                    if len(v14) < len(v2):
                        v2 = v14
            v2[v1] = v2
            return v2
        return helper(0, v1)
