# Time:  O(log(min(m, n)))
# Space: O(1)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def getKth(A, B, k):
            m, n = len(A), len(B)
            if m > n:
                m, n = n, m
                A, B = B, A
            i = binary_search(max(k-n, 0), min(m, k)-1, lambda i: A[i] >= B[k-1-i])
            return max(A[i-1] if i-1 >= 0 else float("-inf"), B[k-1-i] if k-1-i >= 0 else float("-inf"))

        len1, len2 = len(nums1), len(nums2)
        if (len1+len2) % 2 == 1:
            return getKth(nums1, nums2, (len1+len2)//2+1)
        else:
            return (getKth(nums1, nums2, (len1+len2)//2)+getKth(nums1, nums2, (len1+len2)//2+1))*0.5    


