class Solution:
    def rearrangeArray(self, nums):
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        res = []
        for p, n in zip(positives, negatives):
            res.extend([p, n])
        return res
