class C1:

    def countRangeSum(self, a1, a2, a3):
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = len(v1)

        def divide_conquer(a1, a2, a3, a4):
            if a2 - a1 <= 1:
                return 0
            v1 = a1 + (a2 - a1) // 2
            v2 = divide_conquer(a1, v1, a3, a4) + divide_conquer(v1, a2, a3, a4)
            v3 = []
            v4, v5, v6 = (v1, v1, v1)
            for v7 in range(a1, v1):
                while v4 < a2 and v1[v4] - v1[v7] < a3:
                    v4 += 1
                while v5 < a2 and v1[v5] - v1[v7] <= a4:
                    v5 += 1
                v2 += v5 - v4
                while v6 < a2 and v1[v6] < v1[v7]:
                    v3.append(v1[v6])
                    v6 += 1
                v3.append(v1[v7])
            while v6 < a2:
                v3.append(v1[v6])
                v6 += 1
            v1[a1:a2] = v3
            return v2
        return divide_conquer(0, v3, a2, a3)
