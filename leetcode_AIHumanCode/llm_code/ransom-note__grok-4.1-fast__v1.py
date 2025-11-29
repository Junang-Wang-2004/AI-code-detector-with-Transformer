class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0] * 26
        for ch in magazine:
            freq[ord(ch) - ord('a')] += 1
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1
            if freq[idx] < 0:
                return False
        return True
