class C1:

    def findSmallestInteger(self, a1, a2):
        v1 = [0] * a2
        for v2 in a1:
            v1[v2 % a2] += 1
        return min((v1[i] * a2 + i for v3 in range(a2)))
