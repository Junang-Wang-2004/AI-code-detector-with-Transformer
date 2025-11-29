class Solution:
    def maxSumBST(self, root):
        self.answer = 0
        
        def traverse(curr):
            if not curr:
                return True, 0, float('inf'), float('-inf')
            
            left_ok, left_s, left_lo, left_hi = traverse(curr.left)
            right_ok, right_s, right_lo, right_hi = traverse(curr.right)
            
            if left_ok and right_ok and left_hi < curr.val and curr.val < right_lo:
                subsum = left_s + curr.val + right_s
                self.answer = max(self.answer, subsum)
                return True, subsum, min(left_lo, curr.val), max(curr.val, right_hi)
            
            return False, 0, 0, 0
        
        traverse(root)
        return self.answer
