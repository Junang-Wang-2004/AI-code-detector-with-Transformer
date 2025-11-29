class Solution(object):
    def countGoodStrings(self, minimum, maximum, length0, length1):
        mod = 10**9 + 7
        ways = [0] * (maximum + 1)
        ways[0] = 1
        for current_length in range(1, maximum + 1):
            if current_length >= length0:
                ways[current_length] = (ways[current_length] + ways[current_length - length0]) % mod
            if current_length >= length1:
                ways[current_length] = (ways[current_length] + ways[current_length - length1]) % mod
        return sum(ways[minimum:]) % mod
