class Solution(object):
    def minSubarraySort(self, nums, k):
        n = len(nums)
        if k == 1:
            return [0] * n
        def get_keeps(a):
            next_greater = [n] * n
            stack = []
            for p in range(n - 1, -1, -1):
                while stack and a[stack[-1]] < a[p]:
                    stack.pop()
                if stack:
                    next_greater[p] = stack[-1]
                stack.append(p)
            res = []
            last_drop = -1
            cur_left = 0
            for finish in range(1, n):
                if a[finish] < a[finish - 1]:
                    last_drop = finish
                if finish < k - 1:
                    continue
                wleft = max(cur_left, finish - k + 1)
                while wleft < n and next_greater[wleft] <= last_drop:
                    wleft = next_greater[wleft]
                rlen = max(finish - next_greater[wleft] + 1, 0)
                res.append(rlen)
                cur_left = wleft
            return res
        suffix_keeps = get_keeps(nums)
        flipped = [-nums[n - 1 - p] for p in range(n)]
        prefix_keeps = get_keeps(flipped)
        m = n - k + 1
        return [max(k - prefix_keeps[m - 1 - i] - suffix_keeps[i], 0) for i in range(m)]
