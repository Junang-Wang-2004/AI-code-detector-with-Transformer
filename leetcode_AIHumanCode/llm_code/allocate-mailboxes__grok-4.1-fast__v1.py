class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + houses[i]
        
        cost_matrix = [[0] * n for _ in range(n)]
        for start in range(n):
            for finish in range(start, n):
                length = finish - start + 1
                med_index = start + (length - 1) // 2
                left_sum = prefix[med_index] - prefix[start]
                left_count = med_index - start
                right_sum = prefix[finish + 1] - prefix[med_index + 1]
                right_count = finish - med_index
                med_pos = houses[med_index]
                cost_matrix[start][finish] = right_sum - right_count * med_pos + left_count * med_pos - left_sum
        
        INF = 10**18
        dp_table = [[INF] * n for _ in range(k + 1)]
        for idx in range(n):
            dp_table[1][idx] = cost_matrix[0][idx]
        
        for group_count in range(2, k + 1):
            for idx in range(group_count - 1, n):
                for prior in range(group_count - 2, idx):
                    dp_table[group_count][idx] = min(
                        dp_table[group_count][idx],
                        dp_table[group_count - 1][prior] + cost_matrix[prior + 1][idx]
                    )
        
        return dp_table[k][n - 1]
