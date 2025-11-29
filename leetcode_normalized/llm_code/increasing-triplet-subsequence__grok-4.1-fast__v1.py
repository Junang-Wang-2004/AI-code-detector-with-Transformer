class C1:

    def increasingTriplet(self, a1):
        v1 = len(a1)
        v2 = [float('inf')] * v1
        v3 = float('inf')
        for v4 in range(v1):
            v2[v4] = v3
            v3 = min(v3, a1[v4])
        v5 = [float('-inf')] * v1
        v6 = float('-inf')
        for v4 in range(v1 - 1, -1, -1):
            v5[v4] = v6
            v6 = max(v6, a1[v4])
        for v4 in range(1, v1 - 1):
            if v2[v4] < a1[v4] < v5[v4]:
                return True
        return False
