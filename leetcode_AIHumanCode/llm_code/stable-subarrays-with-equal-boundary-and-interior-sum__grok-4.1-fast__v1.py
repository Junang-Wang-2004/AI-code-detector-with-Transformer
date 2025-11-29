from collections import defaultdict

class Solution:
    def countStableSubarrays(self, capacity):
        freq = defaultdict(int)
        ans = 0
        prefix = 0
        for i, num in enumerate(capacity):
            query = prefix - num
            ans += freq[(num, query)]
            prefix += num
            freq[(num, prefix)] += 1
            if num == 0 and i > 0 and capacity[i - 1] == 0:
                ans -= 1
        return ans
