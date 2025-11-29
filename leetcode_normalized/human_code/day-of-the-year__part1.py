class C1(object):

    def __init__(self):

        def dayOfMonth(a1):
            return 28 if a1 == 2 else 31 - (a1 - 1) % 7 % 2
        self.__lookup = [0] * 12
        for v1 in range(1, len(self.__lookup)):
            self.__lookup[v1] += self.__lookup[v1 - 1] + dayOfMonth(v1)

    def dayOfYear(self, a1):
        """
        """
        v1, v2, v3 = list(map(int, a1.split('-')))
        v4 = 1 if v2 > 2 and (v1 % 4 == 0 and v1 % 100 != 0 or v1 % 400 == 0) else 0
        return self.__lookup[v2 - 1] + v3 + v4
