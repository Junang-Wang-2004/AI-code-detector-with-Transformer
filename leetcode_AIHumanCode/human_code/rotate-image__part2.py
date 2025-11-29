# Time:  O(n^2)
# Space: O(n^2)
class Solution2(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]

