import sys
sys.setrecursionlimit(10 ** 5 + 10)

class C1:

    def maxKDivisibleComponents(self, a1, a2, a3, a4):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)

        def compute(a1, a2):
            v1 = a3[a1] % a4
            v2 = 0
            for v3 in v1[a1]:
                if v3 == a2:
                    continue
                v4, v5 = compute(v3, a1)
                v2 += v4
                if v5 == 0:
                    v2 += 1
                else:
                    v1 = (v1 + v5) % a4
            return (v2, v1)
        v5, v2 = compute(0, -1)
        return v5 + 1
