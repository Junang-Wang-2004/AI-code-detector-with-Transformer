class C1(object):

    def checkValidString(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v1 += 1 if v3 == '(' else -1
            v2 -= 1 if v3 == ')' else -1
            if v2 < 0:
                break
            v1 = max(v1, 0)
        return v1 == 0
