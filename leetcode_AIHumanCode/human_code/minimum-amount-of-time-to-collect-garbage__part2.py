# Time:  O(n * l), l = max(len(g) for g in garbage) = O(10)
# Space: O(1)
# simulation, prefix sum
class Solution2(object):
    def garbageCollection(self, garbage, travel):
        """
        """
        result = 0
        for t in 'MPG':
            curr = 0
            for i in range(len(garbage)):
                cnt = garbage[i].count(t) 
                if cnt:
                    result += curr+cnt
                    curr = 0
                if i < len(travel):
                    curr += travel[i]
        return result
