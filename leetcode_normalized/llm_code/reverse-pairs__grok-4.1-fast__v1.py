class C1:

    def reversePairs(self, a1):

        def helper(a1):
            if len(a1) < 2:
                return (0, a1)
            v1 = len(a1) // 2
            v2, v3 = helper(a1[:v1])
            v4, v5 = helper(a1[v1:])
            v6 = 0
            v7 = 0
            for v8 in v3:
                while v7 < len(v5) and v8 > 2 * v5[v7]:
                    v7 += 1
                v6 += v7
            v9 = []
            v10, v11 = (0, 0)
            while v10 < len(v3) and v11 < len(v5):
                if v3[v10] <= v5[v11]:
                    v9.append(v3[v10])
                    v10 += 1
                else:
                    v9.append(v5[v11])
                    v11 += 1
            v9.extend(v3[v10:])
            v9.extend(v5[v11:])
            return (v2 + v4 + v6, v9)
        return helper(a1)[0]
