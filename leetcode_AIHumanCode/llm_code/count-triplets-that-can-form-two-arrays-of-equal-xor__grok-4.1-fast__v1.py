from collections import defaultdict

class Solution:
    def countTriplets(self, arr):
        freq = defaultdict(int)
        total = defaultdict(int)
        freq[0] = 1
        res = 0
        xor = 0
        for pos in range(len(arr)):
            xor ^= arr[pos]
            res += freq[xor] * pos - total[xor]
            freq[xor] += 1
            total[xor] += pos + 1
        return res
