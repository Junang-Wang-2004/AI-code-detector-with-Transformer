class C1:

    def dailyTemperatures(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = []
        for v4 in range(v1 - 1, -1, -1):
            while v3 and a1[v3[-1]] <= a1[v4]:
                v3.pop()
            v2[v4] = v3[-1] - v4 if v3 else 0
            v3.append(v4)
        return v2
