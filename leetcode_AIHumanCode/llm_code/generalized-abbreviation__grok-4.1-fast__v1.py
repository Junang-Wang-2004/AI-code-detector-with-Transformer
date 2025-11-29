class Solution:
    def generateAbbreviations(self, word):
        n = len(word)
        result = []
        for mask in range(1 << n):
            positions = [-1]
            for i in range(n):
                if mask & (1 << i):
                    positions.append(i)
            positions.append(n)
            parts = []
            for j in range(1, len(positions)):
                prev_pos = positions[j - 1]
                curr_pos = positions[j]
                skip_count = curr_pos - prev_pos - 1
                if skip_count > 0:
                    parts.append(str(skip_count))
                if curr_pos < n:
                    parts.append(word[curr_pos])
            result.append(''.join(parts))
        return result
