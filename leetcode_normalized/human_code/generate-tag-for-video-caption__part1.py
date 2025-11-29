class C1(object):

    def generateTag(self, a1):
        """
        """
        v1 = 100
        v2 = ['#']
        for v3 in range(len(a1)):
            if a1[v3] == ' ':
                continue
            v2.append(a1[v3].upper() if v3 == 0 or a1[v3 - 1] == ' ' else a1[v3].lower())
            if len(v2) == v1:
                break
        if 1 < len(v2):
            v2[1] = v2[1].lower()
        return ''.join(v2)
