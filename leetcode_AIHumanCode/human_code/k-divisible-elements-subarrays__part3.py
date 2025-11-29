# Time:  O(n^2)
# Space: O(n)
# rolling hash
class Solution3(object):
    def countDistinct(self, nums, k, p):
        """
        """
        MOD, P = 10**9+7, 200
        result = 0
        cnt, h = [0]*len(nums), [0]*len(nums)
        for l in range(1, len(nums)+1):
            lookup = set()
            for i in range(len(nums)-l+1):
                cnt[i] += (nums[i+l-1]%p == 0)
                if cnt[i] > k:
                    continue
                h[i] = (h[i]*P+nums[i+l-1])%MOD
                lookup.add(h[i])
            result += len(lookup)
        return result
