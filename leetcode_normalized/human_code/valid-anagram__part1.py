import collections

class C1(object):

    def isAnagram(self, a1, a2):
        """
        """
        if len(a1) != len(a2):
            return False
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        for v2 in a2:
            v1[v2] -= 1
            if v1[v2] < 0:
                return False
        return True
