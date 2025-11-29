class C1:

    def largestMagicSquare(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in a1:
            v5 = [0]
            for v6 in v4:
                v5.append(v5[-1] + v6)
            v3.append(v5)
        v7 = []
        for v8 in range(v2):
            v5 = [0]
            for v9 in range(v1):
                v5.append(v5[-1] + a1[v9][v8])
            v7.append(v5)

        def verify_magic(a1, a2, a3):
            v1 = sum((a1[a1 + k][a2 + k] for v2 in range(a3)))
            if sum((a1[a1 + v2][a2 + a3 - 1 - v2] for v2 in range(a3))) != v1:
                return False
            for v3 in range(a1, a1 + a3):
                if v3[v3][a2 + a3] - v3[v3][a2] != v1:
                    return False
            for v4 in range(a2, a2 + a3):
                if v7[v4][a1 + a3] - v7[v4][a1] != v1:
                    return False
            return True
        v10 = min(v1, v2)
        for v11 in range(v10, 0, -1):
            for v12 in range(v1 - v11 + 1):
                for v13 in range(v2 - v11 + 1):
                    if verify_magic(v12, v13, v11):
                        return v11
        return 1
