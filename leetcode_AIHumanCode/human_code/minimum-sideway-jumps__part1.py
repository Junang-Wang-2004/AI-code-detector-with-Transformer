# Time:  O(n)
# Space: O(1)

# greedy solution
class Solution(object):
    def minSideJumps(self, obstacles):
        """
        """
        result, lanes = 0, set([2])
        for i in range(len(obstacles)-1):
            lanes.discard(obstacles[i+1])
            if lanes:
                continue
            result += 1
            lanes = set(j for j in range(1, 4) if j not in [obstacles[i], obstacles[i+1]])
        return result

        
