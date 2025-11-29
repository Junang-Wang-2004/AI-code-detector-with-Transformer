class C1(object):

    def longestConsecutive(self, a1):
        """
        """

        def longestConsecutiveHelper(a1):
            if not a1:
                return (0, 0)
            v1 = longestConsecutiveHelper(a1.left)
            v2 = longestConsecutiveHelper(a1.right)
            v3, v4 = (1, 1)
            if a1.left:
                if a1.left.val == a1.val + 1:
                    v3 = max(v3, v1[0] + 1)
                elif a1.left.val == a1.val - 1:
                    v4 = max(v4, v1[1] + 1)
            if a1.right:
                if a1.right.val == a1.val + 1:
                    v3 = max(v3, v2[0] + 1)
                elif a1.right.val == a1.val - 1:
                    v4 = max(v4, v2[1] + 1)
            self.max_len = max(self.max_len, v4 + v3 - 1)
            return (v3, v4)
        self.max_len = 0
        longestConsecutiveHelper(a1)
        return self.max_len
