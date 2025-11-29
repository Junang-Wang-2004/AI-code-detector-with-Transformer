class Solution:
    def getMaxFunctionValue(self, receiver, k):
        n = len(receiver)
        log_levels = 0
        temp = k + 1
        while temp > 0:
            log_levels += 1
            temp >>= 1
        successors = [[0] * n for _ in range(log_levels)]
        sums = [[0] * n for _ in range(log_levels)]
        for node in range(n):
            successors[0][node] = receiver[node]
            sums[0][node] = node
        for level in range(1, log_levels):
            for node in range(n):
                intermediate = successors[level - 1][node]
                successors[level][node] = successors[level - 1][intermediate]
                sums[level][node] = sums[level - 1][node] + sums[level - 1][intermediate]
        max_sum = 0
        for start_node in range(n):
            path_sum = 0
            position = start_node
            steps_left = k + 1
            level = 0
            while steps_left > 0 and level < log_levels:
                if steps_left & 1:
                    path_sum += sums[level][position]
                    position = successors[level][position]
                steps_left >>= 1
                level += 1
            if path_sum > max_sum:
                max_sum = path_sum
        return max_sum
