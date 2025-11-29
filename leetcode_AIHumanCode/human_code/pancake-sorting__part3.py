# Time:  O(n^2)
# Space: O(1)
class Solution3(object):
    def pancakeSort(self, A):
        """
        """
        def reverse(l, begin, end):
            for i in range((end-begin) // 2):
                l[begin+i], l[end-1-i] = l[end-1-i], l[begin+i]

        result = []
        for n in reversed(range(1, len(A)+1)):
            i = A.index(n)
            reverse(A, 0, i+1)
            result.append(i+1)
            reverse(A, 0, n)
            result.append(n)
        return result
