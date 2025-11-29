class C1(object):

    def countInterestingSubarrays(self, a1, a2, a3):
        v1 = [0] * a2
        v1[0] = 1
        v2 = 0
        v3 = 0
        for v4 in a1:
            v3 = (v3 + (1 if v4 % a2 == a3 else 0)) % a2
            v5 = (v3 - a3) % a2
            v2 += v1[v5]
            v1[v3] += 1
        return v2
