# Time:  O(n)
# Space: O(n)
# Manacher's Algorithm
class Solution3(object):
    def shortestPalindrome(self, s):
        """
        """
        def preProcess(s):
            if not s:
                return ['^', '$']
            string = ['^']
            for c in s:
                string +=  ['#', c]
            string += ['#', '$']
            return string

        string = preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in range(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len = 0
        for i in range(1, len(string) - 1):
            if i - palindrome[i] == 1:
                max_len = palindrome[i]
        return s[len(s)-1:max_len-1:-1] + s

