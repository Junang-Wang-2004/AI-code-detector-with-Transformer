MAXN = 100010
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False

class Solution:
    def splitArray(self, nums):
        length = len(nums)
        prime_total = 0
        overall_total = 0
        for idx in range(length):
            overall_total += nums[idx]
            if is_prime[idx]:
                prime_total += nums[idx]
        return abs(2 * prime_total - overall_total)
