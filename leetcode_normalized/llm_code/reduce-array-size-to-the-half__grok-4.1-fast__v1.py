from collections import Counter

class C1:

    def minSetSize(self, a1):
        v1 = sorted(Counter(a1).values(), reverse=True)
        v2 = (len(a1) + 1) // 2
        v3 = 0
        v4 = 0
        for v5 in v1:
            v4 += v5
            v3 += 1
            if v4 >= v2:
                return v3
        return v3
