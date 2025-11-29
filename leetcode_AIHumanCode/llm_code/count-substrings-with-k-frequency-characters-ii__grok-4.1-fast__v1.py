class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        freq = [0] * 26
        exceed = 0
        start = 0
        safe = 0
        for end in range(n):
            idx = ord(s[end]) - ord('a')
            if freq[idx] == k - 1:
                exceed += 1
            freq[idx] += 1
            while start <= end and exceed > 0:
                jdx = ord(s[start]) - ord('a')
                freq[jdx] -= 1
                if freq[jdx] == k - 1:
                    exceed -= 1
                start += 1
            safe += end - start + 1
        return total - safe
