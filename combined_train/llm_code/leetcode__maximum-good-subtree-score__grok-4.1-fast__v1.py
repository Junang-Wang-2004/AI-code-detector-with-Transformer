class C1:

    def goodSubtreeSum(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [[] for v4 in range(v2)]
        for v5 in range(1, v2):
            v3[a2[v5]].append(v5)
        v6 = [0]

        def get_digits(a1):
            v1 = 0
            while a1:
                v2, a1 = divmod(a1, 10)
                if v1 & 1 << v2:
                    return -1
                v1 |= 1 << v2
            return v1

        def process(a1):
            v1 = {0: 0}
            v2 = get_digits(a1[a1])
            if v2 != -1:
                v1[v2] = a1[a1]
            for v3 in v3[a1]:
                v4 = process(v3)
                v5 = v1.copy()
                for v6, v7 in v1.items():
                    for v8, v9 in v4.items():
                        if v6 & v8 == 0:
                            v10 = v6 | v8
                            v11 = v7 + v9
                            if v10 not in v5 or v5[v10] < v11:
                                v5[v10] = v11
                v1 = v5
            v6[0] = (v6[0] + max(v1.values())) % v1
            return v1
        process(0)
        return v6[0]
