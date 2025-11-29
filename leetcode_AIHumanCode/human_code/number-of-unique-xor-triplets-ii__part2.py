# Time:  O(n^2)
# Space: O(n)
# hash table
class Solution2(object):
    def uniqueXorTriplets(self, nums):
        """
        """
        cnt2, cnt3 = set([0]), set(),  
        max_cnt = 1<<max(nums).bit_length()
        for x in nums:
            for y in cnt2:
                cnt3.add(x^y)
            for y in nums:
                cnt2.add(x^y)
            if len(cnt3) == max_cnt:
                break
        return len(cnt3)
