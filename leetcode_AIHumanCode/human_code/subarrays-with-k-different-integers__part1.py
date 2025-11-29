# Time:  O(n)
# Space: O(k)

import collections


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        """
        def atMostK(A, K):
            count = collections.defaultdict(int)
            result, left = 0, 0
            for right in range(len(A)):
                count[A[right]] += 1
                while len(count) > K:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        count.pop(A[left])
                    left += 1
                result += right-left+1
            return result
        
        return atMostK(A, K) - atMostK(A, K-1)


