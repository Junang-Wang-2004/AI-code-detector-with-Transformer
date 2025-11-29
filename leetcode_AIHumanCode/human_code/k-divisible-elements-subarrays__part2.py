# Time:  O(n^2) on average, worst is O(n^3)
# Space: O(n)
import collections


# rolling hash
class Solution2(object):
    def countDistinct(self, nums, k, p):
        """
        """
        MOD, P = 10**9+7, 113
        def check(nums, lookup, l, i):
            return all(any(nums[i+k] != nums[j+k] for k in range(l)) for j in lookup)

        result = 0
        cnt, h = [0]*len(nums), [0]*len(nums)
        for l in range(1, len(nums)+1):
            lookup = collections.defaultdict(list)
            for i in range(len(nums)-l+1):
                cnt[i] += (nums[i+l-1]%p == 0)
                if cnt[i] > k:
                    continue
                h[i] = (h[i]*P+nums[i+l-1])%MOD
                if not check(nums, lookup[h[i]], l, i):
                    continue
                lookup[h[i]].append(i)
                result += 1
        return result


