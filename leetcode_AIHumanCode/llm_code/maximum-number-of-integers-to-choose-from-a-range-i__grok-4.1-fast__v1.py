class Solution:
    def maxCount(self, banned, n, maxSum):
        forbidden = sorted(b for b in set(banned) if 1 <= b <= n)
        
        def compute_sum_count(mx):
            sumb = 0
            cntb = 0
            for val in forbidden:
                if val > mx:
                    break
                sumb += val
                cntb += 1
            fullsum = mx * (mx + 1) // 2
            return fullsum - sumb, mx - cntb
        
        left = 0
        right = n
        while left < right:
            middle = (left + right + 1) // 2
            cursum, _ = compute_sum_count(middle)
            if cursum <= maxSum:
                left = middle
            else:
                right = middle - 1
        _, count = compute_sum_count(left)
        return count
