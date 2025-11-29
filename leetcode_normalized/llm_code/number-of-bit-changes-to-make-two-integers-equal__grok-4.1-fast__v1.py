class C1:

    def minChanges(self, a1, a2):
        v1 = 0
        while a1 or a2:
            v2 = a2 & 1
            v3 = a1 & 1
            if v2:
                if not v3:
                    return -1
            elif v3:
                v1 += 1
            a1 >>= 1
            a2 >>= 1
        return v1
