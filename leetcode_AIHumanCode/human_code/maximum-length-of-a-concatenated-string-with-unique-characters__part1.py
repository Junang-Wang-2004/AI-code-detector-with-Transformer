# Time:  O(n) ~ O(2^n)
# Space: O(1) ~ O(2^n)

power = [1]
log2 = {1:0}
for i in range(1, 26):
    power.append(power[-1]<<1)
    log2[power[i]] = i


class Solution(object):
    def maxLength(self, arr):
        """
        """
        def bitset(s):
            result = 0
            for c in s:
                if result & power[ord(c)-ord('a')]:
                    return 0
                result |= power[ord(c)-ord('a')]
            return result
        
        def number_of_one(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        dp = [0]
        for x in arr:
            x_set = bitset(x)
            if not x_set:
                continue
            curr_len = len(dp)
            for i in range(curr_len):
                if dp[i] & x_set:
                    continue
                dp.append(dp[i] | x_set)
        return max(number_of_one(s_set) for s_set in dp)


