class C1(object):

    def binaryTreePaths(self, a1):
        v1, v2 = ([], [])
        self.binaryTreePathsRecu(a1, v2, v1)
        return v1

    def binaryTreePathsRecu(self, a1, a2, a3):
        if a1 is None:
            return
        if a1.left is a1.right is None:
            v1 = ''
            for v2 in a2:
                v1 += str(v2.val) + '->'
            a3.append(v1 + str(a1.val))
        if a1.left:
            a2.append(a1)
            self.binaryTreePathsRecu(a1.left, a2, a3)
            a2.pop()
        if a1.right:
            a2.append(a1)
            self.binaryTreePathsRecu(a1.right, a2, a3)
            a2.pop()
