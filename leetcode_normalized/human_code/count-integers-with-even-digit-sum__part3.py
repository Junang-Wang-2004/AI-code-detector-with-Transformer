class C1(object):

    def countEven(self, a1):
        """
        """
        return sum((sum(map(int, str(x))) % 2 == 0 for v1 in range(1, a1 + 1)))
