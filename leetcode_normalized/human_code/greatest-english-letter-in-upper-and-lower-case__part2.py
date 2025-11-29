import itertools
import string

class C1(object):

    def greatestLetter(self, a1):
        """
        """
        v1 = set(a1)
        return next((C for v2, v3 in zip(reversed(string.ascii_lowercase), reversed(string.ascii_uppercase)) if v2 in v1 and v3 in v1), '')
