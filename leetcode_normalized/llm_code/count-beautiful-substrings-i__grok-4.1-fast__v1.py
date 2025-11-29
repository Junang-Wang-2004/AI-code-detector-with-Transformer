from collections import Counter

class C1:

    def beautifulSubstrings(self, a1: str, a2: int) -> int:
        v1 = set('aeiou')
        v2 = len(a1)
        v3 = [0] * (v2 + 1)
        for v4 in range(v2):
            v3[v4 + 1] = v3[v4] + (1 if a1[v4] in v1 else -1)
        v5 = 1
        v6 = a2
        v7 = 0
        while v6 % 2 == 0:
            v7 += 1
            v6 //= 2
        if v7 > 0:
            v5 *= 2 ** ((v7 + 1) // 2 + 1)
        v8 = 3
        while v8 * v8 <= v6:
            v9 = 0
            while v6 % v8 == 0:
                v9 += 1
                v6 //= v8
            if v9 > 0:
                v5 *= v8 ** ((v9 + 1) // 2)
            v8 += 2
        if v6 > 1:
            v5 *= v6 ** ((1 + 1) // 2)
        v10 = Counter()
        v11 = 0
        for v12 in range(v2 + 1):
            v13 = (v3[v12], v12 % v5)
            v11 += v10[v13]
            v10[v13] += 1
        return v11
