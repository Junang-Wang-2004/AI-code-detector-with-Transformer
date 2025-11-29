class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        a = ord('a')
        fr = [0] * 26
        for ch in s:
            fr[ord(ch) - a] += 1
        if sum(f % 2
