import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side
        def get_position(x: int, y: int) -> int:
            if x == 0:
                return y
            if y == side:
                return side + x
            if x == side:
                return 2 * side + (side - y)
            return 3 *
