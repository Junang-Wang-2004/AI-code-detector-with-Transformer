class C1(object):

    def mergeAlternately(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        while v2 < len(a1) or v2 < len(a2):
            if v2 < len(a1):
                v1.append(a1[v2])
            if v2 < len(a2):
                v1.append(a2[v2])
            v2 += 1
        return ''.join(v1)
