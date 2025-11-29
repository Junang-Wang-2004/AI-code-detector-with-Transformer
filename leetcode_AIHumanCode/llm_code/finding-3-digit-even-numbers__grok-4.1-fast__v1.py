import collections

class Solution(object):
    def findEvenNumbers(self, digits):
        freq = collections.Counter(digits)
        ans = []
        for hun in range(1, 10):
            for ten in range(10):
                for unit in range(0, 10, 2):
                    temp = collections.Counter([hun, ten, unit])
                    if all(temp[d] <= freq[d] for d in temp):
                        ans.append(hun * 100 + ten * 10 + unit)
        return ans
