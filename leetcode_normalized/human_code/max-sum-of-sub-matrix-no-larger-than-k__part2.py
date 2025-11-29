class C1(object):

    def maxSumSubmatrix(self, a1, a2):
        """
        """

        class BST(object):

            def __init__(self, a1):
                self.val = a1
                self.left = None
                self.right = None

            def insert(self, a1):
                v1 = self
                while v1:
                    if v1.val >= a1:
                        if v1.left:
                            v1 = v1.left
                        else:
                            v1.left = BST(a1)
                            return
                    elif v1.right:
                        v1 = v1.right
                    else:
                        v1.right = BST(a1)
                        return

            def lower_bound(self, a1):
                v1, v2 = (None, self)
                while v2:
                    if v2.val >= a1:
                        v1, v2 = (v2, v2.left)
                    else:
                        v2 = v2.right
                return v1
        if not a1:
            return 0
        v1 = min(len(a1), len(a1[0]))
        v2 = max(len(a1), len(a1[0]))
        v3 = float('-inf')
        for v4 in range(v1):
            v5 = [0] * v2
            for v6 in range(v4, v1):
                for v7 in range(v2):
                    v5[v7] += a1[v6][v7] if v1 == len(a1) else a1[v7][v6]
                v8 = BST(0)
                v9 = 0
                for sum in v5:
                    v9 += sum
                    v10 = v8.lower_bound(v9 - a2)
                    if v10:
                        v3 = max(v3, v9 - v10.val)
                    v8.insert(v9)
        return v3
