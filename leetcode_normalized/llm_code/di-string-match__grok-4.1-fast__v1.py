class C1:

    def diStringMatch(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        v3, v4 = (0, v1)
        for v5 in range(v1):
            if a1[v5] == 'I':
                v2[v5] = v3
                v3 += 1
            else:
                v2[v5] = v4
                v4 -= 1
        v2[v1] = v3
        return v2
