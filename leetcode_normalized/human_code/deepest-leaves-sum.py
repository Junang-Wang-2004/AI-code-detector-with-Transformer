class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def deepestLeavesSum(self, a1):
        """
        """
        v1 = [a1]
        while v1:
            v2, v1 = (v1, [child for v3 in v1 for v4 in [v3.left, v3.right] if v4])
        return sum((node.val for v5 in v2))
