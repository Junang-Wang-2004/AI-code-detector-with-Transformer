class C1(object):

    def greatestLetter(self, a1):
        """
        """
        v1 = set(a1)
        v2 = ''
        for v3 in a1:
            if v3.isupper() and lower(v3) in a1:
                if v3 > v2:
                    v2 = v3
        return v2
