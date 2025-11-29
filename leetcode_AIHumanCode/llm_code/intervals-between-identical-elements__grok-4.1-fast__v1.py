class Solution:
    def getDistances(self, arr):
        positions = {}
        for idx, val in enumerate(arr):
            if val not in positions:
                positions[val] = []
            positions[val].append(idx)
        answer = [0] * len(arr)
        for ind_list in positions.values():
            m = len(ind_list)
            pre_sum = [0] * (m + 1)
            for t in range(m):
                pre_sum[t + 1] = pre_sum[t] + ind_list[t]
            post_sum = [0] * (m + 1)
            post_sum[m] = 0
            for t in range(m - 1, -1, -1):
                post_sum[t] = ind_list[t] + post_sum[t + 1]
            for t in range(m):
                curr_pos = ind_list[t]
                sum_left = t * curr_pos - pre_sum[t]
                sum_right = post_sum[t + 1] - (m - t - 1) * curr_pos
                answer[curr_pos] = sum_left + sum_right
        return answer
