# Time:  O(max(logk, x)^2)
# Space: O(1)
# bit manipulation, combinatorics
class Solution3(object):
    def findMaximumNumber(self, k, x):
        """
        """
        def floor_log2(x):
            return x.bit_length()-1

        result = prefix_cnt = 0
        while k >= prefix_cnt:
            # l = result.bit_length()
            # assert(prefix_cnt == sum(c == '1' and (l-i)%x == 0 for i, c in enumerate(bin(result)[2:])))
            cnt, i = prefix_cnt, 0
            while (cnt<<1)+(1<<i if (i+1)%x == 0 else 0) <= k:
                cnt = (cnt<<1)+(1<<i if (i+1)%x == 0 else 0)
                i += 1
            k -= cnt
            result += 1<<i
            prefix_cnt += int((i+1)%x == 0)
        return result-1


