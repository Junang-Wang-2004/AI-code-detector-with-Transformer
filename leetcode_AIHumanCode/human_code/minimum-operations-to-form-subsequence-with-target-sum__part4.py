# Time:  O(nlogr)
# Space: O(logr)
# codeforces, https://codeforces.com/problemset/problem/1303/D
# bitmasks, greedy
class Solution4(object):
    def minOperations(self, nums, target):
        """
        """
        def floor_log2_x(x):
            return x.bit_length()-1

        if sum(nums) < target:
            return -1

        cnt = [0]*(floor_log2_x(max(nums))+1)
        for x in nums:
            cnt[floor_log2_x(x)] += 1
        result = i = 0
        while i < len(cnt):
            if target&(1<<i):
                if not cnt[i]:
                    j = next(j for j in range(i, len(cnt)) if cnt[j])
                    result += j-i
                    j = i
                    cnt[i] -= 1
                    continue
                cnt[i] -= 1
            if i+1 < len(cnt):
                cnt[i+1] += cnt[i]//2
            i += 1
        return result
