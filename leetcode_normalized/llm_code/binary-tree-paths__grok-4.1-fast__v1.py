class C1:

    def binaryTreePaths(self, a1):
        if not a1:
            return []
        v1 = [(a1, str(a1.val))]
        v2 = []
        while v1:
            v3, v4 = v1.pop()
            if not v3.left and (not v3.right):
                v2.append(v4)
            if v3.right:
                v1.append((v3.right, v4 + '->' + str(v3.right.val)))
            if v3.left:
                v1.append((v3.left, v4 + '->' + str(v3.left.val)))
        return v2
