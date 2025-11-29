import collections
import string

class C1(object):

    def checkIfCanBreak(self, a1, a2):
        """
        """

        def is_break(a1, a2):
            v1, v2 = (0, 0)
            for v3 in string.ascii_lowercase:
                v1 += a1[v3]
                v2 += a2[v3]
                if v1 < v2:
                    return False
            return True
        v1, v2 = (collections.Counter(a1), collections.Counter(a2))
        return is_break(v1, v2) or is_break(v2, v1)
