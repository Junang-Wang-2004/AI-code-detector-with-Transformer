class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 3
        min_length = n + 1
        start = 0
        for end in range(n):
            char_idx = ord(s[end]) - ord('a')
            freq[char_idx] += 1
            while start <= end and freq[0] >= k and freq[1] >= k and freq[2] >= k:
                min_length = min(min_length, end - start + 1)
                left_idx = ord(s[start]) - ord('a')
                freq[left_idx] -= 1
                start += 1
        return min_length if min_length <= n else -1
