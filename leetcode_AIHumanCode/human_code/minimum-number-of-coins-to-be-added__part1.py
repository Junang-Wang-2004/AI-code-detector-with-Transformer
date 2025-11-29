# Time:  O(nlogn + logt)
# Space: O(1)

# lc0330
# sort, greedy
class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        """
        coins.sort()
        result = reachable = 0
        for x in coins:
            # if x > target:
            #     break
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
            reachable += x
        while not reachable >= target:
            result += 1
            reachable += reachable+1
        return result


