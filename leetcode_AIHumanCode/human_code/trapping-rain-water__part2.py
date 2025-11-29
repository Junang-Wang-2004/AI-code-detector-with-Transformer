# Time:  O(n)
# Space: O(1)
class Solution2(object):
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        for i in range(len(A)):
            if A[top] < A[i]:
                top = i

        second_top = 0
        for i in range(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        second_top = len(A) - 1
        for i in reversed(range(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        return result


