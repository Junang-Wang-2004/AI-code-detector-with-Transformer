# Time:  O(n^2)
# Space: O(n)
# z-function
class Solution_TLE(object):
    def beautifulSplits(self, nums):
        """
        """
        # Template: https://cp-algorithms.com/string/z-function.html
        def z_function(s, left, right):  # Time: O(n), Space: O(n)
            z = [0]*(right-left+1)
            l, r = 0, 0
            for i in range(1, len(z)):
                if i <= r:
                    z[i] = min(r-i+1, z[i-l])
                while i+z[i] < len(z) and s[left+z[i]] == s[left+i+z[i]]:
                    z[i] += 1
                if i+z[i]-1 > r:
                    l, r = i, i+z[i]-1
            return z
        
        result = 0
        z0 = z_function(nums, 0, len(nums)-1)
        for i in range(1, len(nums)-1):
            zi = z_function(nums, i, len(nums)-1)
            for j in range(i+1, len(nums)):
                if (z0[i] >= i and j-i >= i) or zi[j-i] >= j-i:
                    result += 1
        return result
