from collections import Counter

class C1:

    def rearrangeBarcodes(self, a1):
        v1 = Counter(a1)
        v2 = sorted(v1, key=v1.get, reverse=True)
        v3 = [0] * len(a1)
        v4 = 0
        v5 = 1
        for v6 in v2:
            while v1[v6] > 0:
                if v4 < len(v3):
                    v3[v4] = v6
                    v1[v6] -= 1
                    v4 += 2
                elif v5 < len(v3):
                    v3[v5] = v6
                    v1[v6] -= 1
                    v5 += 2
        return v3
