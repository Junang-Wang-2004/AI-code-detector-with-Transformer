class C1(object):

    def checkRecord(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] == 'A':
                v1 += 1
                if v1 == 2:
                    return False
            if v2 < len(a1) - 2 and a1[v2] == a1[v2 + 1] == a1[v2 + 2] == 'L':
                return False
        return True
