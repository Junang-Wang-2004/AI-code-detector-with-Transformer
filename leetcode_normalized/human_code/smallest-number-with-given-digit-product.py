class C1(object):

    def smallestNumber(self, a1):
        """
        """
        v1 = []
        for v2 in reversed(range(2, 9 + 1)):
            while a1 % v2 == 0:
                v1.append(v2)
                a1 //= v2
        return ''.join(map(str, reversed(v1))) or '1' if a1 == 1 else '-1'
