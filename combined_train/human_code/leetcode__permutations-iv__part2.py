class C1(object):

    def permute(self, a1, a2):
        """
        """
        v1 = []
        v2 = [1] * ((a1 - 1 + 1) // 2 + 1)
        for v3 in range(len(v2) - 1):
            v2[v3 + 1] = v2[v3] * (v3 + 1)
        v4 = [False] * a1
        for v3 in range(a1):
            v5 = v2[(a1 - 1 - v3) // 2] * v2[(a1 - 1 - v3 + 1) // 2]
            for v6 in range(a1):
                if not (not v4[v6] and (v3 == 0 and a1 % 2 == 0 or (v6 + 1) % 2 == (1 if not v1 else v1[-1] % 2 ^ 1))):
                    continue
                if a2 <= v5:
                    break
                a2 -= v5
            else:
                return []
            v4[v6] = True
            v1.append(v6 + 1)
        return v1
