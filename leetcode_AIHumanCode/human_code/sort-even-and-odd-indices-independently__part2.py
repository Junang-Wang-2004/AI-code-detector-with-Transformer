# Time:  O(nlogn)
# Space: O(n)
# sort, inplace solution
class Solution2(object):
    def sortEvenOdd(self, nums):
        """
        """
        def partition(index, nums):
            for i in range(len(nums)):
                j = i
                while nums[i] >= 0:
                    j = index(j)
                    nums[i], nums[j] = nums[j], ~nums[i]  # processed
            for i in range(len(nums)):
                nums[i] = ~nums[i]  # restore values
        
        partition(lambda i: i//2 if i%2 == 0 else (len(nums)+1)//2+i//2, nums)
        nums[:(len(nums)+1)//2], nums[(len(nums)+1)//2:] = sorted(nums[:(len(nums)+1)//2]), sorted(nums[(len(nums)+1)//2:], reverse=True)
        partition(lambda i: 2*i if i < (len(nums)+1)//2 else 1+2*(i-(len(nums)+1)//2), nums)
        return nums


