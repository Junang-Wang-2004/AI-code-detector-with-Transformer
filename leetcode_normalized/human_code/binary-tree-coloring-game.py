class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def btreeGameWinningMove(self, a1, a2, a3):
        """
        """

        def count(a1, a2, a3):
            if not a1:
                return 0
            v1, v2 = (count(a1.left, a2, a3), count(a1.right, a2, a3))
            if a1.val == a2:
                a3[0], a3[1] = (v1, v2)
            return v1 + v2 + 1
        v1 = [0, 0]
        count(a1, a3, v1)
        v2 = max(max(v1), a2 - (sum(v1) + 1))
        return v2 > a2 - v2
