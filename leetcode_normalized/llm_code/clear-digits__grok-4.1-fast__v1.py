class C1:

    def clearDigits(self, a1):
        v1 = list(a1)
        v2 = 0
        for v3 in range(len(v1)):
            if 'a' <= v1[v3] <= 'z':
                v1[v2] = v1[v3]
                v2 += 1
            elif v2 > 0:
                v2 -= 1
        return ''.join(v1[:v2])
