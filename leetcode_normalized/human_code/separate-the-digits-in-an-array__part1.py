class C1(object):

    def separateDigits(self, a1):
        """
        """
        v1 = []
        for v2 in reversed(a1):
            while v2:
                v1.append(v2 % 10)
                v2 //= 10
        v1.reverse()
        return v1
