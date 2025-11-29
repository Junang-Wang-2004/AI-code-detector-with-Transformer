# Time:  O(n * l), l = max(len(g) for g in garbage) = O(10)
# Space: O(1)

# simulation, prefix sum
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        """
        result = 0
        lookup = {}
        for i in range(len(garbage)):
            for c in garbage[i]:
                lookup[c] = i
            if i+1 < len(travel):
                travel[i+1] += travel[i]
            result += len(garbage[i])
        result += sum(travel[v-1] for _, v in lookup.items() if v-1 >= 0)
        return result


