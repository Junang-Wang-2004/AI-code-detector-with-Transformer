class C1(object):

    def canChange(self, a1, a2):
        """
        """
        v1 = v2 = 0
        while True:
            while v1 < len(a1) and a1[v1] == '_':
                v1 += 1
            while v2 < len(a2) and a2[v2] == '_':
                v2 += 1
            if v1 == len(a1) and v2 == len(a2):
                break
            if v1 == len(a1) or v2 == len(a2) or a1[v1] != a2[v2] or (a1[v1] == 'L' and v1 < v2) or (a1[v1] == 'R' and v1 > v2):
                return False
            v1 += 1
            v2 += 1
        return True
