class Solution:
    def findMissingRanges(self, nums, lower, upper):
        result = []
        expect = lower
        for val in nums:
            if val > expect:
                if expect == val - 1:
                    result.append(str(expect))
                else:
                    result.append(f"{expect}->{val-1}")
            expect = val + 1
        if upper >= expect:
            if expect == upper:
                result.append(str(expect))
            else:
                result.append(f"{expect}->{upper}")
        return result
