class C1(object):

    def minSwaps(self, a1):

        def digit_sum(a1):
            v1 = 0
            while a1 > 0:
                v1 += a1 % 10
                a1 //= 10
            return v1
        v1 = len(a1)
        v2 = [(digit_sum(a1[i]), a1[i], i) for v3 in range(v1)]
        v4 = sorted(v2)
        v5 = [0] * v1
        for v6, (v7, v7, v8) in enumerate(v4):
            v5[v8] = v6
        v9 = [False] * v1
        v10 = 0
        for v11 in range(v1):
            if not v9[v11]:
                v12 = 0
                v13 = v11
                while not v9[v13]:
                    v9[v13] = True
                    v12 += 1
                    v13 = v5[v13]
                v10 += v12 - 1
        return v10
