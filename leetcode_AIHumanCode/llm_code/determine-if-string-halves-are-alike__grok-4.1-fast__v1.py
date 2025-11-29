class Solution:
    def halvesAreAlike(self, s):
        vowels = set('aeiouAEIOU')
        n = len(s)
        mid = n // 2
        left_count = sum(c in vowels for c in s[:mid])
        right_count = sum(c in vowels for c in s[mid:])
        return left_count == right_count
