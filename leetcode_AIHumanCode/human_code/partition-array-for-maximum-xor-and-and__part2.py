# Time:  O(nlogr * 2^n)
# Space: O(1)
# bitmasks, greedy
class Solution2(object):
    def maximizeXorAndXor(self, nums):
        """
        """
        def max_xor_subset(nums):  # Time: O(nlogr)
            base = [0]*l 
            for x in nums:  # gaussian elimination over GF(2)
                for i in reversed(range(len(base))):
                    if not x&(1<<i):
                        continue
                    if base[i] == 0:
                        base[i] = x
                        break
                    x ^= base[i]
            max_xor = 0
            for b in reversed(base):  # greedy
                if (max_xor^b) > max_xor:
                    max_xor ^= b
            return max_xor

        l = max(nums).bit_length()
        n = len(nums)
        result = 0
        for mask in range(1, 1<<n):
            and_arr = -1
            xor_arr = 0
            for i in range(n):
                if mask&(1<<i):
                    and_arr = and_arr&nums[i] if and_arr != -1 else nums[i]
                else:
                    xor_arr ^= nums[i]
            max_xor = max_xor_subset(((nums[i]&~xor_arr) for i in range(n) if not (mask&(1<<i))))
            result = max(result, and_arr+xor_arr+2*max_xor)
        return result
