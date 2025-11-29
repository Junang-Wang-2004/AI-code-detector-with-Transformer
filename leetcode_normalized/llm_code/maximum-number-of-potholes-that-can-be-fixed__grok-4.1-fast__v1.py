class C1:

    def maxPotholes(self, a1, a2):
        v1 = [len(run) for v2 in a1.split('.') if v2]
        v1.sort(reverse=True)
        v3 = 0
        v4 = a2
        for v5 in v1:
            v6 = v5 + 1
            v7 = min(v6, v4)
            v8 = v7 - 1
            if v8 <= 0:
                break
            v3 += v8
            v4 -= v7
        return v3
