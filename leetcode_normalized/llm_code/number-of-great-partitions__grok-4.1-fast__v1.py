class C1:

    def countPartitions(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = sum(a1)
        if v2 < 2 * a2:
            return 0
        v3 = [1] + [0] * (a2 - 1)
        for v4 in a1:
            v5 = [0] * a2
            for v6 in range(a2):
                v5[v6] = v3[v6]
                if v6 >= v4:
                    v5[v6] = (v5[v6] + v3[v6 - v4]) % v1
            v3 = v5
        v7 = sum(v3) % v1
        v8 = pow(2, len(a1), v1)
        return (v8 - 2 * v7) % v1
