class C1(object):

    def beautifulSubstrings(self, a1, a2):
        """
        """
        v1 = set('aeiou')
        v2 = 0
        for v3 in range(len(a1)):
            v4 = v5 = 0
            for v6 in range(v3, len(a1)):
                if a1[v6] in v1:
                    v5 += 1
                else:
                    v4 += 1
                if v4 == v5 and v4 * v5 % a2 == 0:
                    v2 += 1
        return v2
