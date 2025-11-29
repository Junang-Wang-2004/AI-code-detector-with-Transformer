class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        req = [0] * 26
        for char in s1:
            req[ord(char) - ord('a')] += 1
        win = [0] * 26
        k = len(s1)
        for j in range(k):
            win[ord(s2[j]) - ord('a')] += 1
        if win == req:
            return True
        for j in range(k, len(s2)):
            win[ord(s2[j]) - ord('a')] += 1
            idx = ord(s2[j - k]) - ord('a')
            win[idx] -= 1
            if win == req:
                return True
        return False
