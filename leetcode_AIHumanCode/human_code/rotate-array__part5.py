# Time:  O(k * n)
# Space: O(1)
class Solution5(object):
    """
    """
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

 
