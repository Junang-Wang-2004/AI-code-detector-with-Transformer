class Solution:
    def maximumPrimeDifference(self, nums):
        MAX_VAL = 100
        is_prime = [True] * (MAX_VAL + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX_VAL ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_VAL + 1, i):
                    is_prime[j] = False
        earliest = -1
        latest = -1
        for pos in range(len(nums)):
            val = nums[pos]
            if val <= MAX_VAL and is_prime[val]:
                if earliest == -1:
                    earliest = pos
                latest = pos
        return latest - earliest
