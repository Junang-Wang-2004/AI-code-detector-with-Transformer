class C1(object):

    def largestValues(self, a1):
        """
        """
        v1 = []
        v2 = [a1]
        while any(v2):
            v1.append(max((node.val for v3 in v2)))
            v2 = [child for v3 in v2 for v4 in (v3.left, v3.right) if v4]
        return v1
