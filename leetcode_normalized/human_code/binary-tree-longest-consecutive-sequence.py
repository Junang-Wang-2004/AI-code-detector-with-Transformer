class C1(object):

    def longestConsecutive(self, a1):
        """
        """
        self.max_len = 0

        def longestConsecutiveHelper(a1):
            if not a1:
                return 0
            v1 = longestConsecutiveHelper(a1.left)
            v2 = longestConsecutiveHelper(a1.right)
            v3 = 1
            if a1.left and a1.left.val == a1.val + 1:
                v3 = max(v3, v1 + 1)
            if a1.right and a1.right.val == a1.val + 1:
                v3 = max(v3, v2 + 1)
            self.max_len = max(self.max_len, v3)
            return v3
        longestConsecutiveHelper(a1)
        return self.max_len
