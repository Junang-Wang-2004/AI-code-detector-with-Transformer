class C1:

    def largestEvenSum(self, a1, a2):
        v1 = sorted(a1, reverse=True)
        v2 = sum(v1[:a2])
        if v2 % 2 == 0:
            return v2
        v3 = float('inf')
        v4 = float('inf')
        for v5 in v1[:a2]:
            if v5 % 2 == 0:
                v3 = min(v3, v5)
            else:
                v4 = min(v4, v5)
        v6 = float('-inf')
        v7 = float('-inf')
        for v5 in v1[a2:]:
            if v5 % 2 == 0:
                v6 = max(v6, v5)
            else:
                v7 = max(v7, v5)
        v8 = []
        if v4 != float('inf') and v6 != float('-inf'):
            v8.append(v2 - v4 + v6)
        if v3 != float('inf') and v7 != float('-inf'):
            v8.append(v2 - v3 + v7)
        return max(v8) if v8 else -1
