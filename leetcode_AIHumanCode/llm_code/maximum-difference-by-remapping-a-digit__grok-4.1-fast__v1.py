class Solution:
    def minMaxDifference(self, num):
        s = str(num)
        max_digit = next((ch for ch in s if ch != '9'), None)
        min_digit = next((ch for ch in s if ch != '0'), None)
        max_str = ''.join('9' if ch == max_digit else ch for ch in s) if max_digit else s
        min_str = ''.join('0' if ch == min_digit else ch for ch in s) if min_digit else s
        return int(max_str) - int(min_str)
