class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        m = n - k + 1
        if m < 3:
            return []
        windows = [prefix[j + k] - prefix[j] for j in range(m)]

        left_maxes = [0.0] * m
        left_positions = [0] * m
        left_maxes[0] = windows[0]
        left_positions[0] = 0
        for j in range(1, m):
            if windows[j] > left_maxes[j - 1]:
                left_maxes[j] = windows[j]
                left_positions[j] = j
            else:
                left_maxes[j] = left_maxes[j - 1]
                left_positions[j] = left_positions[j - 1]

        right_maxes = [0.0] * m
        right_positions = [0] * m
        right_maxes[m - 1] = windows[m - 1]
        right_positions[m - 1] = m - 1
        for j in range(m - 2, -1, -1):
            if windows[j] > right_maxes[j + 1]:
                right_maxes[j] = windows[j]
                right_positions[j] = j
            else:
                right_maxes[j] = right_maxes[j + 1]
                right_positions[j] = right_positions[j + 1]

        max_total = 0
        result = []
        for mid in range(k, n - 2 * k + 1):
            l_idx = mid - k
            r_idx = mid + k
            current = (left_maxes[l_idx] + windows[mid] +
                       right_maxes[r_idx])
            if current > max_total:
                max_total = current
                result = [left_positions[l_idx], mid,
                          right_positions[r_idx]]
        return result
