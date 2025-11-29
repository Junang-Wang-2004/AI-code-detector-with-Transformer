class C1:

    def getMaxGridHappiness(self, a1: int, a2: int, a3: int, a4: int) -> int:
        v1 = a1 * a2
        v2 = [0] * v1
        v3 = [0]

        def compute_delta(a1: int, a2: int, a3: int) -> int:
            v1 = -30 * ((a2 == 1) + (a3 == 1)) + 20 * ((a2 == 2) + (a3 == 2))
            v2 = (a2 != 0) + (a3 != 0)
            if a1 == 1:
                return v1 + 120 - 30 * v2
            if a1 == 2:
                return v1 + 40 + 20 * v2
            return 0

        def search(a1: int, a2: int, a3: int, a4: int):
            if a1 == v1 or (a2 == 0 and a3 == 0):
                v3[0] = max(v3[0], a4)
                return
            if a4 + 120 * (a2 + a3) < v3[0]:
                return
            v1 = a1 - 1 if a1 % a2 else -1
            v2 = a1 - a2 if a1 >= a2 else -1
            v3 = v2[v1] if v1 >= 0 else 0
            v4 = v2[v2] if v2 >= 0 else 0
            v5 = v3 or v4
            if a2 > 0:
                v6 = compute_delta(1, v3, v4)
                v2[a1] = 1
                search(a1 + 1, a2 - 1, a3, a4 + v6)
                v2[a1] = 0
            if a3 > 0:
                v6 = compute_delta(2, v3, v4)
                v2[a1] = 2
                search(a1 + 1, a2, a3 - 1, a4 + v6)
                v2[a1] = 0
            if v5:
                search(a1 + 1, a2, a3, a4)
        search(0, a3, a4, 0)
        return v3[0]
