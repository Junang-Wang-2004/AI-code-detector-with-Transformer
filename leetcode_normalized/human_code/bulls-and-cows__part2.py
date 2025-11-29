import operator
from collections import defaultdict, Counter

class C1(object):

    def getHint(self, a1, a2):
        """
        """
        v1 = sum(map(operator.eq, a1, a2))
        v2 = sum((Counter(a1) & Counter(a2)).values()) - v1
        return '%dA%dB' % (v1, v2)
