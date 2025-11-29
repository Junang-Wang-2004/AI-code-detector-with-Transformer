class C1:

    def numRescueBoats(self, a1, a2):
        a1.sort(reverse=True)
        v1 = 0
        v2 = 0
        v3 = len(a1) - 1
        while v2 <= v3:
            v1 += 1
            if a1[v2] + a1[v3] <= a2 and v2 < v3:
                v2 += 1
                v3 -= 1
            else:
                v2 += 1
        return v1
