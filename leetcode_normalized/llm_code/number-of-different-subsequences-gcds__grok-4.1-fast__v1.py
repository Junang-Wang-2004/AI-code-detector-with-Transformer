import math

class C1:

    def countDifferentSubsequenceGCDs(self, a1):
        v1 = max(a1)
        v2 = [False] * (v1 + 1)
        for v3 in a1:
            v2[v3] = True
        v4 = 0
        for v5 in range(1, v1 + 1):
            v6 = 0
            v7 = v5
            while v7 <= v1:
                if v2[v7]:
                    v6 = math.gcd(v6, v7)
                    if v6 == v5:
                        v4 += 1
                        break
                v7 += v5
        return v4
