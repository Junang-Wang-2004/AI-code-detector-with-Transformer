class C1:

    def largestDivisibleSubset(self, a1):
        if not a1:
            return []
        a1.sort()
        v1 = len(a1)
        v2 = [[a1[i]] for v3 in range(v1)]
        for v3 in range(v1):
            for v4 in range(v3):
                if a1[v3] % a1[v4] == 0 and len(v2[v3]) < len(v2[v4]) + 1:
                    v2[v3] = v2[v4][:] + [a1[v3]]
        return max(v2, key=len)
