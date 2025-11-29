import collections
import bisect

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(list)

    def set(self, a1, a2, a3):
        """
        """
        self.lookup[a1].append((a3, a2))

    def get(self, a1, a2):
        """
        """
        v1 = self.lookup.get(a1, None)
        if v1 is None:
            return ''
        v2 = bisect.bisect_right(v1, (a2 + 1, 0))
        return v1[v2 - 1][1] if v2 else ''
