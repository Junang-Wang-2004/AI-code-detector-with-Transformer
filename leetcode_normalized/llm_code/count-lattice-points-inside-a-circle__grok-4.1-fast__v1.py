class C1:

    def countLatticePoints(self, a1):
        v1 = min((cx - rad for v2, v3, v4 in a1))
        v5 = max((v2 + v4 for v2, v3, v4 in a1))
        v6 = min((cy - v4 for v3, v7, v4 in a1))
        v8 = max((v7 + v4 for v3, v7, v4 in a1))
        v9 = set()
        for v10 in range(v1, v5 + 1):
            for v11 in range(v6, v8 + 1):
                for v2, v7, v4 in a1:
                    if (v10 - v2) ** 2 + (v11 - v7) ** 2 <= v4 ** 2:
                        v9.add((v10, v11))
                        break
        return len(v9)
