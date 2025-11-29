import itertools

class C1(object):

    def luckyNumbers(self, a1):
        """
        """
        return list(set(map(min, a1)) & set(map(max, zip(*a1))))
