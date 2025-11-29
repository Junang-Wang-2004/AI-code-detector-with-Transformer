class C1(object):

    def minSubArrayLen(self, a1, a2):
        v1 = 0
        sum = 0
        v2 = float('inf')
        for v3 in range(len(a2)):
            sum += a2[v3]
            while sum >= a1:
                v2 = min(v2, v3 - v1 + 1)
                sum -= a2[v1]
                v1 += 1
        return v2 if v2 != float('inf') else 0
