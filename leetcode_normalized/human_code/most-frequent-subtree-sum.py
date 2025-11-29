import collections

class C1(object):

    def findFrequentTreeSum(self, a1):
        """
        """

        def countSubtreeSumHelper(a1, a2):
            if not a1:
                return 0
            v1 = a1.val + countSubtreeSumHelper(a1.left, a2) + countSubtreeSumHelper(a1.right, a2)
            a2[v1] += 1
            return v1
        v1 = collections.defaultdict(int)
        countSubtreeSumHelper(a1, v1)
        v2 = max(v1.values()) if v1 else 0
        return [total for v3, v4 in v1.items() if v4 == v2]
