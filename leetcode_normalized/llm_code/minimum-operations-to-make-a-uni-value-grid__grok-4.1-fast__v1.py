class C1:

    def minOperations(self, a1, a2):
        v1 = []
        for v2 in a1:
            v1.extend(v2)
        v3 = {v % a2 for v4 in v1}
        if len(v3) > 1:
            return -1
        v1.sort()
        v5 = v1[len(v1) // 2]
        v6 = 0
        for v4 in v1:
            v6 += abs(v4 - v5) // a2
        return v6
