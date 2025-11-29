class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        occupied_positions = [i for i, s in enumerate(seats) if s]
        if not occupied_positions:
            return 0
        ans = occupied_positions[0]
        ans = max(ans, n - 1 - occupied_positions[-1])
        for k in range(1, len(occupied_positions)):
            ans = max(ans, (occupied_positions[k] - occupied_positions[k - 1]) // 2)
        return ans
