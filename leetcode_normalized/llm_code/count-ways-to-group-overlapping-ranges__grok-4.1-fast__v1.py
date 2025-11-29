class C1:

    def countWays(self, a1):
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = []
        for v3 in a1:
            if not v2 or v3[0] > v2[-1][1]:
                v2.append(v3)
            else:
                v2[-1][1] = max(v2[-1][1], v3[1])
        return pow(2, len(v2), v1)
