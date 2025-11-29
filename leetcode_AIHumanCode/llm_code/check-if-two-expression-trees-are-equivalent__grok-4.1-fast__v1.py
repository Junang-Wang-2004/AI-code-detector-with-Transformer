class Solution:
    def checkEquivalence(self, root1, root2):
        def compute_freq(tree):
            freq = [0] * 26
            def traverse(n):
                if not n:
                    return
                if n.val.isalpha():
                    freq[ord(n.val) - ord('a')] += 1
                traverse(n.left)
                traverse(n.right)
            traverse(tree)
            return freq
        return compute_freq(root1) == compute_freq(root2)
