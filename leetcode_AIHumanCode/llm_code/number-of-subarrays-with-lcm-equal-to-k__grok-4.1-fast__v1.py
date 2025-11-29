import math
from collections import defaultdict

class Solution:
    def subarrayLCM(self, nums, k):
        def lcm(a, b):
            return a * b // math.gcd(a, b)

        freq = defaultdict(int)
        answer = 0
        for num in nums:
            if k % num != 0:
                freq.clear()
                continue
            new_freq = defaultdict(int)
            new_freq[num] += 1
            for prev, cnt in freq.items():
                new_freq[lcm(prev, num)] += cnt
            freq = new_freq
            answer += freq[k]
        return answer
