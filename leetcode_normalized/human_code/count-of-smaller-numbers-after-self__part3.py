class C1(object):

    def countSmaller(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = self.BST()
        for v3 in reversed(range(len(a1))):
            v2.insertNode(a1[v3])
            v1[v3] = v2.query(a1[v3])
        return v1

    class BST(object):

        class BSTreeNode(object):

            def __init__(self, a1):
                self.val = a1
                self.count = 0
                self.left = self.right = None

        def __init__(self):
            self.root = None

        def insertNode(self, a1):
            v1 = self.BSTreeNode(a1)
            if not self.root:
                self.root = v1
                return
            v2 = self.root
            while v2:
                if v1.val < v2.val:
                    v2.count += 1
                    if v2.left:
                        v2 = v2.left
                    else:
                        v2.left = v1
                        break
                elif v2.right:
                    v2 = v2.right
                else:
                    v2.right = v1
                    break

        def query(self, a1):
            v1 = 0
            v2 = self.root
            while v2:
                if a1 < v2.val:
                    v2 = v2.left
                elif a1 > v2.val:
                    v1 += 1 + v2.count
                    v2 = v2.right
                else:
                    return v1 + v2.count
            return 0
