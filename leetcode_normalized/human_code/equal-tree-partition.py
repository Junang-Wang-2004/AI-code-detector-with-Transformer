import collections

class C1(object):

    def checkEqualTree(self, a1):
        """
        """

        def getSumHelper(a1, a2):
            if not a1:
                return 0
            v1 = a1.val + getSumHelper(a1.left, a2) + getSumHelper(a1.right, a2)
            a2[v1] += 1
            return v1
        v1 = collections.defaultdict(int)
        v2 = getSumHelper(a1, v1)
        if v2 == 0:
            return v1[v2] > 1
        return v2 % 2 == 0 and v2 / 2 in v1
