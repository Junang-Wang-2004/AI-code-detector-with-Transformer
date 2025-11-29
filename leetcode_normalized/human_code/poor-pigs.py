import math

class C1(object):

    def poorPigs(self, a1, a2, a3):
        """
        """
        return int(math.ceil(math.log(a1) / math.log(a3 / a2 + 1)))
