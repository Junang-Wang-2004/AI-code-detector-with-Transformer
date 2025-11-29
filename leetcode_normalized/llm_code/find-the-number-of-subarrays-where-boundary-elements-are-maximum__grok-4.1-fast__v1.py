class C1:

    def numberOfSubarrays(self, a1):
        v1 = 0
        v2 = []
        for v3 in a1:
            while v2 and v2[-1][0] < v3:
                v4, v5 = v2.pop()
                v1 += v5 * (v5 + 1) // 2
            if v2 and v2[-1][0] == v3:
                v2[-1][1] += 1
            else:
                v2.append([v3, 1])
        for v4, v5 in v2:
            v1 += v5 * (v5 + 1) // 2
        return v1
