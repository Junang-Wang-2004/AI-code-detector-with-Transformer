class C1(object):

    def lowestCommonAncestor(self, a1, a2):
        """
        """

        def depth(a1):
            v1 = 0
            while a1:
                a1 = a1.parent
                v1 += 1
            return v1
        v1, v2 = (depth(a1), depth(a2))
        while v1 > v2:
            a1 = a1.parent
            v1 -= 1
        while v1 < v2:
            a2 = a2.parent
            v2 -= 1
        while a1 != a2:
            a1 = a1.parent
            a2 = a2.parent
        return a1
