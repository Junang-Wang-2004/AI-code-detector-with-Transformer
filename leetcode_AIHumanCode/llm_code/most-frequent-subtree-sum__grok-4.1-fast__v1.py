class Solution:
    def findFrequentTreeSum(self, root):
        freq = {}
        def traverse(node):
            if node is None:
                return 0
            lsum = traverse(node.left)
            rsum = traverse(node.right)
            cursum = node.val + lsum + rsum
            freq[cursum] = freq.get(cursum, 0) + 1
            return cursum
        if root is not None:
            traverse(root)
        if not freq:
            return []
        highest = max(freq.values())
        result = [sum_val for sum_val, cnt in freq.items() if cnt == highest]
        return result
