class C1(object):

    def generateKey(self, a1, a2, a3):
        """
        """
        v1 = 4
        v2 = 0
        v3 = pow(10, v1 - 1)
        for v4 in range(v1):
            v2 = v2 * 10 + min(a1 // v3 % 10, a2 // v3 % 10, a3 // v3 % 10)
            v3 //= 10
        return v2
