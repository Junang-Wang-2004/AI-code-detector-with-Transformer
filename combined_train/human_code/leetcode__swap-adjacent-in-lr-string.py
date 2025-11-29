class C1(object):

    def canTransform(self, a1, a2):
        """
        """
        if a1.count('X') != a2.count('X'):
            return False
        v1, v2 = (0, 0)
        while v1 < len(a1) and v2 < len(a2):
            while v1 < len(a1) and a1[v1] == 'X':
                v1 += 1
            while v2 < len(a2) and a2[v2] == 'X':
                v2 += 1
            if (v1 < len(a1)) != (v2 < len(a2)):
                return False
            elif v1 < len(a1) and v2 < len(a2):
                if a1[v1] != a2[v2] or (a1[v1] == 'L' and v1 < v2) or (a1[v1] == 'R' and v1 > v2):
                    return False
            v1 += 1
            v2 += 1
        return True
