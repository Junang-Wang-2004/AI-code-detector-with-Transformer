class C1(object):

    def checkIfExist(self, a1):
        """
        """
        v1 = set()
        for v2 in a1:
            if 2 * v2 in v1 or (v2 % 2 == 0 and v2 // 2 in v1):
                return True
            v1.add(v2)
        return False
