class C1(object):

    def earliestFullBloom(self, a1, a2):
        """
        """
        v1 = list(range(len(a2)))
        v1.sort(key=lambda x: a2[x], reverse=True)
        v2 = v3 = 0
        for v4 in v1:
            v3 += a1[v4]
            v2 = max(v2, v3 + a2[v4])
        return v2
