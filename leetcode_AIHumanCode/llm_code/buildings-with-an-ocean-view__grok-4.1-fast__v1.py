class Solution:
    def findBuildings(self, heights):
        buildings = []
        max_height = 0
        n = len(heights)
        for j in range(n - 1, -1, -1):
            if heights[j] > max_height:
                buildings.append(j)
                max_height = heights[j]
        buildings.reverse()
        return buildings
