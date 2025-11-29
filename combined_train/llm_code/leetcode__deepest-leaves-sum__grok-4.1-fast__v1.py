class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def deepestLeavesSum(self, a1):
        if not a1:
            return 0
        v1 = [a1]
        while v1:
            v2 = []
            for v3 in v1:
                if v3.left:
                    v2.append(v3.left)
                if v3.right:
                    v2.append(v3.right)
            if not v2:
                return sum((v3.val for v3 in v1))
            v1 = v2
