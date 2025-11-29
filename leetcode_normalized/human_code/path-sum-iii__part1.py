import collections

class C1(object):

    def pathSum(self, a1, a2):
        """
        """

        def pathSumHelper(a1, a2, a3, a4):
            if a1 is None:
                return 0
            a2 += a1.val
            v2 = a4[a2 - a3] if a2 - a3 in a4 else 0
            a4[a2] += 1
            v2 += pathSumHelper(a1.left, a2, a3, a4) + pathSumHelper(a1.right, a2, a3, a4)
            a4[a2] -= 1
            if a4[a2] == 0:
                del a4[a2]
            return v2
        v1 = collections.defaultdict(int)
        v1[0] = 1
        return pathSumHelper(a1, 0, a2, v1)
