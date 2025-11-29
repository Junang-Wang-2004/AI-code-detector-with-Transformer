from collections import Counter

class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        total_count = Counter(nums)
        prefix_count = Counter()
        answer = 0
        for value in nums:
            target = 2 * value
            suffix_count = total_count[target] - prefix_count[target]
            answer = (answer + prefix_count[target] * suffix_count) % MOD
            prefix_count[value] += 1
        return answer
