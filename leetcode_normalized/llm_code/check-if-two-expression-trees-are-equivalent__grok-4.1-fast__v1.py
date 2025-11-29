class C1:

    def checkEquivalence(self, a1, a2):

        def compute_freq(a1):
            v1 = [0] * 26

            def traverse(a1):
                if not a1:
                    return
                if a1.val.isalpha():
                    v1[ord(a1.val) - ord('a')] += 1
                traverse(a1.left)
                traverse(a1.right)
            traverse(a1)
            return v1
        return compute_freq(a1) == compute_freq(a2)
