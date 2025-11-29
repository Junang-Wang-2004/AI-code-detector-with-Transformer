from collections import defaultdict

class C1:

    def longestEqualSubarray(self, a1, a2):
        v1 = defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)
        v4 = 0
        for v5 in v1.values():
            v6 = len(v5)
            v7 = 0
            for v8 in range(v6):
                while v7 < v6 and v5[v7] <= v5[v8] + (v7 - v8) + a2:
                    v7 += 1
                v4 = max(v4, v7 - v8)
        return v4
