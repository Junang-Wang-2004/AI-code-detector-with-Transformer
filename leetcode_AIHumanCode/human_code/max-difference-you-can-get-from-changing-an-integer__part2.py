# Time:  O(logn)
# Space: O(logn)
# greedy
class Solution2(object):
    def maxDiff(self, num):
        """
        """
        digits = str(num)
        b = next((x for x in digits if x < '9'), '0')
        a = next((x for x in digits if x > '1'), '0')
        return int(digits.replace(b, '9'))-int(digits.replace(a, '1' if digits[0] != '1' else '0'))
