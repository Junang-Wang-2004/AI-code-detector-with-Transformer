import itertools

class C1(object):

    def selfDividingNumbers(self, a1, a2):
        """
        """
        return [num for v1 in range(a1, a2 + 1) if not any(map(lambda x: int(x) == 0 or v1 % int(x) != 0, str(v1)))]
