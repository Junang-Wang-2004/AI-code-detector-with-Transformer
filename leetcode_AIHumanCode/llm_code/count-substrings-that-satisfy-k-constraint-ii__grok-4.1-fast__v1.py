class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries) -> list[int]:
        n = len(s)
        min_start = [0] * n
        num_ones = 0
        begin = 0
        for finish in range(n):
            num_ones += (s[finish] == '1')
            while num_ones > k and (finish - begin + 1 - num_ones) > k:
                num_ones -= (s[begin] == '1')
                begin += 1
            min_start[finish] = begin
        
        totals = [0] * (n + 1)
        for finish in range(n):
            totals[finish + 1] = totals[finish] + (finish - min_start[finish] + 1)
        
        max_reach = [-1] * n
        furthest = -1
        for pos in range(n):
            while furthest + 1 < n and min_start[furthest + 1] <= pos:
                furthest += 1
            max_reach[pos] = furthest
        
        def triangle_size(length):
            return length * (length + 1) // 2
        
        answers = []
        for start_idx, end_idx in queries:
            max_pos = min(max_reach[start_idx], end_idx)
            first_part = triangle_size(max_pos - start_idx + 1)
            second_part = totals[end_idx + 1] - totals[max_pos + 1]
            answers.append(first_part + second_part)
        return answers
