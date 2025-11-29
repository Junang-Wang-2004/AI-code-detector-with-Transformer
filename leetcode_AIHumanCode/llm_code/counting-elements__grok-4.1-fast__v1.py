class Solution:
    def countElements(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        res = 0
        for num in freq:
            if num + 1 in freq:
                res += freq[num]
        return res
