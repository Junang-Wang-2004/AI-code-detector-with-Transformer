# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def largestSumAfterKNegations(self, A, K):
        """
        """
        A.sort()
        remain = K
        for i in range(K):
            if A[i] >= 0:
                break
            A[i] = -A[i]
            remain -= 1
        return sum(A) - (remain%2)*min(A)*2
