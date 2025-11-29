class Solution:
    def lastNonEmptyString(self, s):
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        max_freq = max(counts)
        visited = [False] * 26
        output = []
        for pos in range(len(s) - 1, -1, -1):
            char_idx = ord(s[pos]) - ord('a')
            if not visited[char_idx] and counts[char_idx] == max_freq:
                output.append(s[pos])
                visited[char_idx] = True
        return ''.join(output[::-1])
