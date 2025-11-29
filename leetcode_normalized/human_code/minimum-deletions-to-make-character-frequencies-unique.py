import collections
import string

class C1(object):

    def minDeletions(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = 0
        v3 = set()
        for v4 in string.ascii_lowercase:
            for v5 in reversed(range(1, v1[v4] + 1)):
                if v5 not in v3:
                    v3.add(v5)
                    break
                v2 += 1
        return v2
