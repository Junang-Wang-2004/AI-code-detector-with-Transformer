class C1:

    def separateSquares(self, a1):
        if not a1:
            return 0.0
        v1 = min((y for v2, v3, v2 in a1))
        v4 = max((v3 + l for v2, v3, v5 in a1))
        v6 = sum((v5 * v5 for v2, v2, v5 in a1))
        v7 = v6 / 2.0

        def area_under(a1):
            v1 = 0.0
            for v2, v3, v4 in a1:
                if a1 > v3:
                    if a1 >= v3 + v4:
                        v1 += v4 * v4
                    else:
                        v1 += v4 * (a1 - v3)
            return v1
        v8, v9 = (v1, v4)
        while v9 - v8 > 1e-10:
            v10 = (v8 + v9) / 2
            if area_under(v10) >= v7:
                v9 = v10
            else:
                v8 = v10
        return v8
