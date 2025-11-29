class C1:

    def maxAlternatingSum(self, a1):
        v1 = [val * val for v2 in a1]
        v1.sort(reverse=True)
        v3 = (len(a1) + 1) // 2
        v4 = sum(v1[:v3])
        v5 = sum(v1[v3:])
        return v4 - v5
