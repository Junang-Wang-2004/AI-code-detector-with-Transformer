# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def maxSizeSlices(self, slices):
        """
        """
        def maxSizeSlicesLinear(slices, start, end):
            dp = [[0]*(len(slices)//3+1) for _ in range(3)]
            for i in range(start, end):
                for j in range(1, min(((i-start+1)-1)//2+1, len(slices)//3)+1):
                    dp[i%3][j] = max(dp[(i-1)%3][j], dp[(i-2)%3][j-1] + slices[i])
            return dp[(end-1)%3][len(slices)//3]
        
        return max(maxSizeSlicesLinear(slices, 0, len(slices)-1),
                   maxSizeSlicesLinear(slices, 1, len(slices)))
