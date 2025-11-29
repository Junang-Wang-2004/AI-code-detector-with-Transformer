class C1(object):

    def countNumbers(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = 100
        v3 = [0] * (v2 + 1)
        v3[1] = 1
        for v4 in range(2, v2 + 1):
            v3[v4] = v1 - v1 // v4 * v3[v1 % v4] % v1

        def binom(a1, a2, a3):
            if a2 == 0:
                return 1
            if a1 < 0 or a2 < 0 or a2 > a1:
                return 0
            v1 = 1
            for v2 in range(a2):
                v1 = v1 * ((a1 - v2) % a3) % a3
            for v2 in range(1, a2 + 1):
                v1 = v1 * v3[v2] % a3
            return v1

        def count_max(a1, a2, a3):
            if a1 < 0:
                return 0
            v1 = []
            v2 = a1
            while v2:
                v1.append(v2 % a2)
                v2 //= a2
            v1.reverse()
            if not v1:
                v1 = [0]
            v3 = len(v1)
            v4 = 0
            v5 = True
            v6 = 0
            for v7 in range(v3):
                v8 = v1[v7]
                if v7 > 0 and v6 > v8:
                    v5 = False
                    break
                v9 = v6
                if v9 < v8:
                    v10 = v3 - v7 - 1
                    v11 = a2 - (v8 - 1)
                    v12 = a2 - v9
                    v13 = v11 + v10 - 1
                    v14 = v12 + v10 - 1
                    v15 = (binom(v14 + 1, v10 + 1, a3) - binom(v13, v10 + 1, a3) + a3) % a3
                    v4 = (v4 + v15) % a3
                v6 = v8
            if v5:
                v4 = (v4 + 1) % a3
            return v4
        return (count_max(int(a2), a3, v1) - count_max(int(a1) - 1, a3, v1) + v1) % v1
