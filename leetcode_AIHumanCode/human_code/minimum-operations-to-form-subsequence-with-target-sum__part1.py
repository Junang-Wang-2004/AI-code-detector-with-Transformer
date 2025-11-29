# Time:  O(n)
# Space: O(logn)

# codeforces, https://codeforces.com/problemset/problem/1303/D
# counting sort, greedy
class Solution(object):
    def minOperations(self, nums, target):
        """
        """
        def floor_log2_x(x):
            return x.bit_length()-1

        total = sum(nums)
        if total < target:
            return -1

        cnt = [0]*(floor_log2_x(max(nums))+1)
        for x in nums:
            cnt[floor_log2_x(x)] += 1
        result = 0
        for i in reversed(range(len(cnt))):
            for _ in range(cnt[i]):
                x = 1<<i
                if x <= target:
                    target -= x
                    total -= x
                elif total-x >= target:
                    total -= x
                else:
                    cnt[i-1] += 2
                    result += 1
        return result


