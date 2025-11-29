class C1(object):

    def compareSub(self, a1, a2, a3, a4):
        pass

    def length(self):
        pass

class C2(object):

    def getIndex(self, a1):
        """
        """
        v1, v2 = (0, a1.length() - 1)
        while v1 < v2:
            v3 = v1 + (v2 - v1) // 2
            if a1.compareSub(v1, v3, v3 if (v2 - v1 + 1) % 2 else v3 + 1, v2) >= 0:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
