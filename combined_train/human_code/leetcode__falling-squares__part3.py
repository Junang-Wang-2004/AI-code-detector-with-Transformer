class C1(object):

    def fallingSquares(self, a1):

        def query(a1, a2, a3, a4, a5, a6):
            v1 = 0
            while a2 % a4 and a2 <= a3:
                v1 = max(v1, a1[a2], a5[a2 // a4])
                a2 += 1
            while a3 % a4 != a4 - 1 and a2 <= a3:
                v1 = max(v1, a1[a3], a5[a3 // a4])
                a3 -= 1
            while a2 <= a3:
                v1 = max(v1, a5[a2 // a4], a6[a2 // a4])
                a2 += a4
            return v1

        def update(a1, a2, a3, a4, a5, a6, a7):
            while a2 % a4 and a2 <= a3:
                a1[a2] = max(a1[a2], a7)
                a6[a2 // a4] = max(a6[a2 // a4], a7)
                a2 += 1
            while a3 % a4 != a4 - 1 and a2 <= a3:
                a1[a3] = max(a1[a3], a7)
                a6[a3 // a4] = max(a6[a3 // a4], a7)
                a3 -= 1
            while a2 <= a3:
                a5[a2 // a4] = max(a5[a2 // a4], a7)
                a2 += a4
        v1 = set()
        for v2, v3 in a1:
            v1.add(v2)
            v1.add(v2 + v3 - 1)
        v1 = sorted(list(v1))
        v4 = len(v1)
        v5 = int(v4 ** 0.5)
        v6 = [0] * v4
        v7 = [0] * (v5 + 2)
        v8 = [0] * (v5 + 2)
        v9 = 0
        v10 = []
        for v2, v3 in a1:
            v11, v12 = (bisect.bisect_left(v1, v2), bisect.bisect_left(v1, v2 + v3 - 1))
            v13 = query(v6, v11, v12, v5, v7, v8) + v3
            update(v6, v11, v12, v5, v7, v8, v13)
            v9 = max(v9, v13)
            v10.append(v9)
        return v10
