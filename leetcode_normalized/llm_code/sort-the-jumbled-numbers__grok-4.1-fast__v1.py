class C1:

    def sortJumbled(self, a1, a2):

        def remap(a1):
            v1 = 0
            v2 = 1
            for v3 in str(a1)[::-1]:
                v4 = int(v3)
                v1 += a1[v4] * v2
                v2 *= 10
            return v1
        v1 = sorted(range(len(a2)), key=lambda idx: remap(a2[idx]))
        return [a2[i] for v2 in v1]
