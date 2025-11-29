class C1(object):

    def permute(self, a1, a2):
        """
        """
        v1 = []
        v2 = [1] * a1
        for v3 in range(len(v2) - 1):
            v2[v3 + 1] = min(v2[v3] * ((v3 + 2) // 2), a2)
        v4 = [False] * a1
        for v3 in range(a1):
            for v5 in range(a1):
                if not (not v4[v5] and (v3 == 0 and a1 % 2 == 0 or (v5 + 1) % 2 == (1 if not v1 else v1[-1] % 2 ^ 1))):
                    continue
                if a2 <= v2[a1 - 1 - v3]:
                    break
                a2 -= v2[a1 - 1 - v3]
            else:
                return []
            v4[v5] = True
            v1.append(v5 + 1)
        return v1
