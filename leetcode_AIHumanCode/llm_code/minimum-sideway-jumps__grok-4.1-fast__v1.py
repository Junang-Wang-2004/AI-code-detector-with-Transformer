class Solution:
    def minSideJumps(self, obstacles):
        lane1, lane2, lane3 = 1, 0, 1
        for block in obstacles:
            if block == 1:
                lane1 = float('inf')
            if block == 2:
                lane2 = float('inf')
            if block == 3:
                lane3 = float('inf')
            new_lane1 = min(lane1, lane2 + 1, lane3 + 1) if block != 1 else float('inf')
            new_lane2 = min(lane1 + 1, lane2, lane3 + 1) if block != 2 else float('inf')
            new_lane3 = min(lane1 + 1, lane2 + 1, lane3) if block != 3 else float('inf')
            lane1, lane2, lane3 = new_lane1, new_lane2, new_lane3
        return min(lane1, lane2, lane3)
