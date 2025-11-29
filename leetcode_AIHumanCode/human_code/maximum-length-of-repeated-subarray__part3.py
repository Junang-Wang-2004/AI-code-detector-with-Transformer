# Time:  O(m * n * min(m, n) * log(min(m, n)))
# Space: O(min(m^2, n^2))
# Binary search (122 ms)
class Solution3(object):
    def findLength(self, A, B):
        """
        """
        if len(A) > len(B): return self.findLength(B, A)

        def check(length):
            lookup = set(A[i:i+length] \
                       for i in range(len(A)-length+1))
            return any(B[j:j+length] in lookup \
                       for j in range(len(B)-length+1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = left + (right-left)/2
            if not check(mid):  # find the min idx such that check(idx) == false
                right = mid
            else:
                left = mid+1
        return left-1

