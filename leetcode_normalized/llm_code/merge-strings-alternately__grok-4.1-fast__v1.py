class C1:

    def mergeAlternately(self, a1, a2):
        v1 = min(len(a1), len(a2))
        v2 = ''.join((a1[k] + a2[k] for v3 in range(v1)))
        if len(a1) > len(a2):
            v2 += a1[v1:]
        else:
            v2 += a2[v1:]
        return v2
