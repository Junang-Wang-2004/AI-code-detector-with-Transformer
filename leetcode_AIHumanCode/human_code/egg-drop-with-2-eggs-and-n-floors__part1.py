# Time:  O(1)
# Space: O(1)

import math


# see the proof: https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/
class Solution(object):
    def twoEggDrop(self, n):
        """
        """
        return int(math.ceil((-1+(1+8*n)**0.5)/2))
    

