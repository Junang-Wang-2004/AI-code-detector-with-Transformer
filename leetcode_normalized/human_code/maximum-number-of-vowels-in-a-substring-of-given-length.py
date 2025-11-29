class C1(object):

    def maxVowels(self, a1, a2):
        """
        """
        v1 = set('aeiou')
        v2 = v3 = 0
        for v4, v5 in enumerate(a1):
            v3 += v5 in v1
            if v4 >= a2:
                v3 -= a1[v4 - a2] in v1
            v2 = max(v2, v3)
        return v2
