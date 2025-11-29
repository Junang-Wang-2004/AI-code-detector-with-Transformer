class Solution(object):
    def minOperations(self, nums):
        highest = 0
        for n in nums:
            cnt = 0
            m = n
            while m:
                cnt += 1
                m >>= 1
            if cnt > highest:
                highest = cnt
        total = 0
        for n in nums:
            cnt = 0
            m = n
            while m:
                if m & 1:
                    cnt += 1
                m >>= 1
            total += cnt
        return total + max(0, highest - 1)
