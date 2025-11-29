class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def rangeSumBST(self, a1, a2, a3):
        """
        """
        v1 = 0
        v2 = [a1]
        while v2:
            v3 = v2.pop()
            if v3:
                if a2 <= v3.val <= a3:
                    v1 += v3.val
                if a2 < v3.val:
                    v2.append(v3.left)
                if v3.val < a3:
                    v2.append(v3.right)
        return v1
