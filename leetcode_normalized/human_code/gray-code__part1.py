class C1(object):

    def grayCode(self, a1):
        """
        """
        v1 = [0]
        for v2 in range(a1):
            for a1 in reversed(v1):
                v1.append(1 << v2 | a1)
        return v1
