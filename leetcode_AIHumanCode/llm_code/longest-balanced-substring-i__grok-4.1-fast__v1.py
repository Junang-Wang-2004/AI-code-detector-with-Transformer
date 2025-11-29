class Solution:
    def longestBalanced(self, s):
        n = len(s)
        answer = 0
        for start_pos in range(n):
            frequencies = [0] * 26
            num_distinct = 0
            highest = 0
            sub_length = 0
            end_pos = start_pos
            while end_pos < n:
                char_index = ord(s[end_pos]) - ord('a')
                if frequencies[char_index] == 0:
                    num_distinct += 1
                frequencies[char_index] += 1
                highest = max(highest, frequencies[char_index])
                sub_length += 1
                if sub_length % num_distinct == 0 and sub_length // num_distinct == highest:
                    answer = max(answer, sub_length)
                end_pos += 1
        return answer
