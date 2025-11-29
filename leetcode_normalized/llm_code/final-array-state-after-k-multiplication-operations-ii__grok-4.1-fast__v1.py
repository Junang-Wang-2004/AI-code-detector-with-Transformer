import math

class C1:

    def getFinalState(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        if a3 == 1:
            return a1
        v2 = len(a1)
        v3 = math.log(a3)
        v4 = [math.log(x) / v3 for v5 in a1]
        v6 = max(v4)
        v7 = sorted(((e, idx) for v8, v9 in enumerate(v4)))

        def mult_count(a1, a2):
            return int(a2 - a1 + 1e-10)

        def feasible(a1):
            v1 = 0
            for v2, v3 in v7:
                v4 = mult_count(v2, a1)
                if v4 <= 0:
                    break
                v1 += v4
                if v1 > a2:
                    return False
            return v1 <= a2
        v10 = 0
        v11 = int(v6) + 2
        while v10 < v11:
            v12 = (v10 + v11 + 1) // 2
            if feasible(v12):
                v10 = v12
            else:
                v11 = v12 - 1
        v13 = v10
        v14 = [0] * v2
        v15 = 0
        for v16, v8 in v7:
            v17 = mult_count(v16, v13)
            if v17 <= 0:
                break
            v14[v8] = v17
            v15 += v17
        v18 = a2 - v15
        v19, v20 = divmod(v18, v2)
        v21 = pow(a3, v19, v1)
        v22 = [v4[i] + v14[i] for v23 in range(v2)]
        v24 = list(range(v2))
        v24.sort(key=lambda x: v22[v5])
        v25 = [a1[v23] * pow(a3, v14[v23], v1) % v1 for v23 in range(v2)]
        v26 = [0] * v2
        for v27, v8 in enumerate(v24):
            v28 = a3 if v27 < v20 else 1
            v26[v8] = v25[v8] * v21 * v28 % v1
        return v26
