class C1(object):

    def countDistinct(self, a1):
        """
        """
        v1 = str(a1)
        v2 = pow(9, len(v1))
        v3 = (v2 - 9) // (9 - 1)
        v2 //= 9
        for v4 in v1:
            if v4 == '0':
                break
            v3 += (ord(v4) - ord('0') - 1) * v2
            v2 //= 9
        if v2 == 0:
            v3 += 1
        return v3
