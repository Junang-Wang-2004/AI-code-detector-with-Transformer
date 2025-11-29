from collections import Counter

class Solution:
    def rearrangeBarcodes(self, codes):
        freq = Counter(codes)
        order = sorted(freq, key=freq.get, reverse=True)
        ans = [0] * len(codes)
        even = 0
        odd = 1
        for num in order:
            while freq[num] > 0:
                if even < len(ans):
                    ans[even] = num
                    freq[num] -= 1
                    even += 2
                elif odd < len(ans):
                    ans[odd] = num
                    freq[num] -= 1
                    odd += 2
        return ans
