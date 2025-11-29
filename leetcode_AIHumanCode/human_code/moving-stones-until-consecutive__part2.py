# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def numMovesStones(self, a, b, c):
        """
        """
        stones = [a, b, c]
        stones.sort()
        left, min_moves = 0, float("inf")
        max_moves = (stones[-1]-stones[0]) - (len(stones)-1)
        for right in range(len(stones)):
            while stones[right]-stones[left]+1 > len(stones): # find window size <= len(stones)
                left += 1
            min_moves = min(min_moves, len(stones)-(right-left+1))  # move stones not in this window
        return [min_moves, max_moves]
