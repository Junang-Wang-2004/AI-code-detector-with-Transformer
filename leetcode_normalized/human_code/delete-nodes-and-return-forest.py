class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def delNodes(self, a1, a2):
        """
        """

        def delNodesHelper(a1, a2, a3, a4):
            if not a2:
                return None
            v1 = a2.val in a1
            if a3 and (not v1):
                a4.append(a2)
            a2.left = delNodesHelper(a1, a2.left, v1, a4)
            a2.right = delNodesHelper(a1, a2.right, v1, a4)
            return None if v1 else a2
        v1 = []
        v2 = set(a2)
        delNodesHelper(v2, a1, True, v1)
        return v1
