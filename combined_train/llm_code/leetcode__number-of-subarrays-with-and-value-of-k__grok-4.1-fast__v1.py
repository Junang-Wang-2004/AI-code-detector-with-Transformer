class C1:

    def countSubarrays(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            if a1[v2] & a2 != a2:
                v2 += 1
                continue
            v4 = {}
            v5 = v2
            while v5 < v3:
                v6 = a1[v5]
                if v6 & a2 != a2:
                    break
                v7 = {}
                v7[v6] = v7.get(v6, 0) + 1
                for v8, v9 in v4.items():
                    v10 = v8 & v6
                    v7[v10] = v7.get(v10, 0) + v9
                v1 += v7.get(a2, 0)
                v4 = v7
                v5 += 1
            v2 = v5
        return v1
