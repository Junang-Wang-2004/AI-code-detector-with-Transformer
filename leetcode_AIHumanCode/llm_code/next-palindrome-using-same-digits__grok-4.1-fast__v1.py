class Solution(object):
    def nextPalindrome(self, num):
        s = list(num)
        n = len(s)
        half = n // 2
        pivot = half - 2
        while pivot >= 0 and s[pivot] >= s[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return ""
        successor = half - 1
        while successor > pivot and s[successor] <= s[pivot]:
            successor -= 1
        s[pivot], s[successor] = s[successor], s[pivot]
        s[pivot + 1:half] = s[pivot + 1:half][::-1]
        rev_left = s[:half][::-1]
        if n % 2 == 0:
            s[half:] = rev_left
        else:
            s[half + 1:] = rev_left
        return "".join(s)
