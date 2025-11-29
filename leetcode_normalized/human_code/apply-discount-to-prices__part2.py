from functools import reduce

class C1(object):

    def discountPrices(self, a1, a2):
        """
        """

        def format(a1, a2):
            return '${:d}.{:02d}'.format(*divmod(int(a2[1:]) * (100 - a1), 100)) if a2[0] == '$' and a2[1:].isdigit() else a2
        return ' '.join((format(a2, x) for v1 in a1.split()))
