class Solution(object):
    def twoEggDrop(self, n):
        left, right = 0, n
        while left < right:
            middle = (left + right) // 2
            if middle * (middle + 1) // 2 >= n:
                right = middle
            else:
                left = middle + 1
        return left
