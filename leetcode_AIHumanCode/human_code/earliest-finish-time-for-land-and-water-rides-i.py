# Time:   O(n)
# Spacee: O(1)

# greedy
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        """
        mn_land = min(landStartTime[i]+landDuration[i] for i in range(len(landStartTime)))
        mn_water = min(waterStartTime[i]+waterDuration[i] for i in range(len(waterStartTime)))
        return min(min(max(landStartTime[i], mn_water)+landDuration[i] for i in range(len(landStartTime))), 
                   min(max(waterStartTime[i], mn_land)+waterDuration[i] for i in range(len(waterStartTime))))
