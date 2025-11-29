class C1:

    def countUnivalSubtrees(self, a1):
        self.total = 0

        def check_subtree(a1):
            if not a1:
                return True
            v1 = check_subtree(a1.left)
            v2 = check_subtree(a1.right)
            v3 = v1 and v2 and (a1.left is None or a1.val == a1.left.val) and (a1.right is None or a1.val == a1.right.val)
            if v3:
                self.total += 1
                return True
            return False
        check_subtree(a1)
        return self.total
