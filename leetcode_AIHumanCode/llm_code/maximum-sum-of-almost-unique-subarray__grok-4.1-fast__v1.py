class Solution(object):
    def maxSum(self, nums, m, k):
        n = len(nums)
        if n < k:
            return 0
        ans = 0
        cur_sum = 0
        dist_cnt = 0
        cnt = {}
        # Build first window
        for i in range(k):
            num = nums[i]
            cur_sum += num
            if num not in cnt:
                cnt[num] = 1
                dist_cnt += 1
            else:
                cnt[num] += 1
        if dist_cnt >= m:
            ans = cur_sum
        # Slide the window
        for i in range(k, n):
            # Add new element
            num = nums[i]
            cur_sum += num
            if num not in cnt:
                cnt[num] = 1
                dist_cnt += 1
            else:
                cnt[num] += 1
            # Remove outgoing element
            old = nums[i - k]
            cnt[old] -= 1
            if cnt[old] == 0:
                dist_cnt -= 1
            cur_sum -= old
            # Update answer
            if dist_cnt >= m:
                ans = max(ans, cur_sum)
        return ans
