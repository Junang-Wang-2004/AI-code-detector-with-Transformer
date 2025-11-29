import collections

class C1(object):

    def findDuplicateSubtrees(self, a1):
        """
        """

        def getid(a1, a2, a3):
            if not a1:
                return -1
            v1 = a2[a1.val, getid(a1.left, a2, a3), getid(a1.right, a2, a3)]
            a3[v1].append(a1)
            return v1
        v1 = collections.defaultdict(list)
        v2 = collections.defaultdict()
        v2.default_factory = v2.__len__
        getid(a1, v2, v1)
        return [roots[0] for v3 in v1.values() if len(v3) > 1]
