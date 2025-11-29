class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)
        mid = length // 2
        counts = [0] * 26
        for ch in s[:mid]:
            counts[ord(ch) - ord('a')] += 1
        front = ''
        base = ord('a')
        for idx in range(26):
            front += chr(base + idx) * counts[idx]
        rev_front = front[::-1]
        if length % 2:
            return front + s[mid] + rev_front
        return front + rev_front
