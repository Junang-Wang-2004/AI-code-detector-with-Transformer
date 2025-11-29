class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sortedArrayToBST(self, a1):
        """
        """
        return self.sortedArrayToBSTRecu(a1, 0, len(a1))

    def sortedArrayToBSTRecu(self, a1, a2, a3):
        if a2 == a3:
            return None
        v1 = a2 + self.perfect_tree_pivot(a3 - a2)
        v2 = C1(a1[v1])
        v2.left = self.sortedArrayToBSTRecu(a1, a2, v1)
        v2.right = self.sortedArrayToBSTRecu(a1, v1 + 1, a3)
        return v2

    def perfect_tree_pivot(self, a1):
        """
        Find the point to partition n keys for a perfect binary search tree
        """
        v1 = 1
        v1 = 1 << a1.bit_length() - 1
        if v1 // 2 - 1 <= a1 - v1:
            return v1 - 1
        else:
            return a1 - v1 // 2
