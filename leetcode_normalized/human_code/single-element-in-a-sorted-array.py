class C1(object):

    def singleNonDuplicate(self, a1):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) / 2
            if not (v3 % 2 == 0 and v3 + 1 < len(a1) and (a1[v3] == a1[v3 + 1])) and (not (v3 % 2 == 1 and a1[v3] == a1[v3 - 1])):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return a1[v1]
