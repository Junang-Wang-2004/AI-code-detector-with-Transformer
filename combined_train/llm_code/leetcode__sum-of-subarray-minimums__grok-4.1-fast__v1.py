class C1:

    def sumSubarrayMins(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [-1] * v2
        v4 = []
        for v5 in range(v2):
            while v4 and a1[v4[-1]] >= a1[v5]:
                v4.pop()
            v3[v5] = v4[-1] if v4 else -1
            v4.append(v5)
        v6 = [v2] * v2
        v4 = []
        for v5 in range(v2 - 1, -1, -1):
            while v4 and a1[v4[-1]] > a1[v5]:
                v4.pop()
            v6[v5] = v4[-1] if v4 else v2
            v4.append(v5)
        v7 = 0
        for v5 in range(v2):
            v8 = v5 - v3[v5]
            v9 = v6[v5] - v5
            v7 = (v7 + a1[v5] * v8 * v9) % v1
        return v7
