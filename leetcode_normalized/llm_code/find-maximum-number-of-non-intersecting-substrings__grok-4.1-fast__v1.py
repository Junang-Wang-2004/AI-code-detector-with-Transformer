class C1:

    def maxSubstrings(self, a1):
        v1 = 0
        v2 = len(a1)
        v3 = 0
        while v3 < v2:
            v4 = {}
            v5 = v3
            v6 = False
            while v5 < v2:
                v7 = a1[v5]
                if v7 in v4:
                    if v5 - v4[v7] + 1 >= 4:
                        v1 += 1
                        v3 = v5 + 1
                        v6 = True
                        break
                else:
                    v4[v7] = v5
                v5 += 1
            if not v6:
                break
        return v1
