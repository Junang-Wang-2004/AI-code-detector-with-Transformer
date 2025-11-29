class Solution(object):
    def largestGoodInteger(self, num):
        if len(num) < 3:
            return ''
        max_digit = ''
        begin = 0
        n = len(num)
        i = 1
        while i <= n:
            if i == n or num[i] != num[begin]:
                if i - begin >= 3:
                    max_digit = max(max_digit, num[begin])
                begin = i
            i += 1
        return max_digit * 3
