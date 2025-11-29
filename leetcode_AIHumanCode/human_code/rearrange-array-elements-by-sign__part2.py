# Time:  O(n)
# Space: O(1)
# generator
class Solution2(object):
    def rearrangeArray(self, nums):
        """
        """
        def pos():
            for x in nums:
                if x > 0:
                    yield x
        
        def neg():
            for x in nums:
                if x < 0:
                    yield x
        
        gen_pos = pos()
        gen_neg = neg()
        return [next(gen_pos) if i%2 == 0 else next(gen_neg)  for i in range(len(nums))]


