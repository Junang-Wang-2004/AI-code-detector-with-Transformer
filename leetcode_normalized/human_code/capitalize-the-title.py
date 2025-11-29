class C1(object):

    def capitalizeTitle(self, a1):
        """
        """
        a1 = list(a1)
        v2 = 0
        for v3 in range(len(a1) + 1):
            if v3 < len(a1) and a1[v3] != ' ':
                a1[v3] = a1[v3].lower()
                continue
            if v3 - v2 > 2:
                a1[v2] = a1[v2].upper()
            v2 = v3 + 1
        return ''.join(a1)
