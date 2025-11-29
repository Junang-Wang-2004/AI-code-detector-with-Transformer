class C1(object):

    def largestOddNumber(self, a1):
        """
        """
        for v1 in reversed(range(len(a1))):
            if int(a1[v1]) % 2:
                return a1[:v1 + 1]
        return ''
